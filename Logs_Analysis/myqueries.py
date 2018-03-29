#for python

import psycopg2
import sys

def get_data(query):
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(query)
    posts = c.fetchall()
    db.close()
    return posts

def most_popular_three_articles():
    query01 = (
    "SELECT articles.title, count(*) AS PV "
    "FROM articles, log "
    "WHERE articles.slug = substr(log.path,10) "
    "AND log.status = '200 OK' "
    "GROUP BY articles.title "
    "ORDER BY PV DESC "
    "LIMIT 3;")
    result = get_data(query01)
    print("<The most popular three articles of all time>")
    print
    for i in range(0, len(result)):
        print ("%s - %d Views" %(result[i][0], result[i][1]))
    print

def most_popular_article_authors():
    query02 = (
    "SELECT name, PV FROM "
    "(SELECT authors.name, count(*) as PV " #Set PV
    "FROM articles, authors, log "
    "WHERE substr(log.path,10) = articles.slug "
    "AND log.status = '200 OK' "
    "GROUP BY authors.name) AS subq01 "
    "WHERE PV>1000000 " #select PV > 1000000
    "ORDER BY PV "
    "DESC;")
    result = get_data(query02)
    print("<The most popular article authors of all time>")
    print
    for i in range(0, len(result)):
        print ("%s - %d Views" %(result[i][0], result[i][1]))
    print

def the_days_that_requests_lead_to_error():
    query03_01 = (
      "SELECT count(*) AS error, date(log.time) "
      "FROM log "
      "WHERE log.status = '404 NOT FOUND' "
      "GROUP BY date(log.time) "
      "ORDER BY date(log.time) ASC;"
      )
    result03_01 = get_data(query03_01)

    query03_02 = (
    "SELECT count(*) AS total, date(log.time) "
    "FROM log "
    "GROUP BY date(log.time);"
    )
    result03_02 = get_data(query03_02)

    query03_03 = (
    "SELECT date(log.time) "
    "FROM log "
    "GROUP BY date(log.time) "
    )
    result03_03 = get_data(query03_03)

    print ("<The days more than 1% of requests lead to errors>")

    error_rate = list()
    for i in range(len(result03_01)):
        calc_error_rate = (float)((float)(result03_01[i][0]*100)/(float)(result03_02[i][0]))
        error_rate.append(calc_error_rate)

    for i in range(len(error_rate)):
        if error_rate[i] > 1.0 :
            sys.stdout.write("%s - %s" %(result03_01[i][1], format(error_rate[i], '.2f')))
            sys.stdout.write("% errors")

if __name__ == '__main__':
    print
    most_popular_three_articles()
    print
    most_popular_article_authors()
    print
    the_days_that_requests_lead_to_error()
    print
    print
