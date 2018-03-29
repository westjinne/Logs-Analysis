#for python
#query02_lil exists

import psycopg2

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
        print result[i]
    print

def most_popular_article_authors():
    query02_lil = (
    "SELECT authors.name, count(*) AS PV "
    "FROM authors, articles, log "
    "WHERE authors.id = articles.author "
    "AND substr(log.path, 10) = articles.slug "
    "AND log.status = '200 OK' "
    "GROUP BY authors.name "
    "ORDER BY PV DESC;")

    query02 = (
    "SELECT name, PV FROM "
    "(SELECT name, count(*) as PV "
    "FROM articles, authors, log "
    "WHERE substr(log.path,10) = articles.slug "
    "AND log.status = '200 OK' "
    "GROUP BY authors.name) AS FOO "
    "WHERE PV>100000000000 "
    "ORDER BY PV "
    "DESC;")
    result = get_data(query02)
    result01 = get_data(query02_lil)
    print("<The most popular article authors of all time>")
    print result
    print result01
    #>1000

def the_days_that_requests_lead_to_error():
#    query03 = ""
#    result = get_data(query03)
    print("<The days more than 1% of requests lead to errors>")

if __name__ == '__main__':
    print
    most_popular_three_articles()
    print
    most_popular_article_authors()
    print
