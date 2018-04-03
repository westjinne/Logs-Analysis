#! /usr/bin/env python

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
    query01 = """
            SELECT articles.title, count(*) AS PV
            FROM articles INNER JOIN log
            ON '/article/' || articles.slug = log.path
            AND log.status = '200 OK'
            GROUP BY articles.title
            ORDER BY PV DESC
            LIMIT 3;
            """
    result = get_data(query01)
    print("<The most popular three articles of all time>")

    for title, views in result:
        print ("%s - %d Views" % (title, views))


def most_popular_article_authors():
    query02 = """
            SELECT authors.name, count(*) AS PV
            FROM authors, log, articles
            WHERE '/article/' || articles.slug = log.path
            AND log.status = '200 OK'
            AND authors.id = articles.author
            GROUP BY authors.name
            ORDER BY PV
            DESC;
            """
    result = get_data(query02)
    print("<The most popular article authors of all time>")

    for author, views in result:
        print ("%s - %d Views" % (author, views))


def the_days_that_requests_lead_to_error():
    query_prac01 = """
        SELECT count(*) AS total
        FROM log
        GROUP BY date(log.time)
    """
    prac01 = get_data(query_prac01)

#    for t in prac01:
#        print("%d" % t)

    query_prac02 = """
        SELECT count(*) AS error, date(log.time) AS day
        FROM log
        WHERE log.status = '404 NOT FOUND'
        GROUP BY day
        ORDER BY day ASC
    """
    prac02 = get_data(query_prac02)

#    for er, to in prac02:
#        print("%d, %s" % (er, to))

    query_last = """
        SELECT date(log.time), round((cnt_error.error*100/cnt_total.total),3) AS perc
        FROM log, (
            SELECT date(log.time) AS day, count(*) as error
            FROM log
            WHERE log.status = '404 NOT FOUND'
            GROUP BY date(log.time)
        ) AS cnt_error, (
            SELECT date(log.time) AS day, count(*) as total
            FROM log
            GROUP BY date(log.time)
        ) AS cnt_total
        WHERE cnt_error.error*100/cnt_total.total::float >= 1
        AND date(log.time) = cnt_total.day
        AND date(log.time) = cnt_error.day
        GROUP BY date(log.time), cnt_error.error, cnt_total.total
        ORDER BY date(log.time)
    """
    last = get_data(query_last)

    for d, r in last:
          print("%s, %f" % (d, r))

#    for title, views in result:
#        print ("%s - %d Views" % (title, views))

#    for i in range(0, len(result)):

#        print ("%s - %d Views" %(result[i][0], result[i][1]))



if __name__ == '__main__':
#    most_popular_three_articles()
#    print
#    most_popular_article_authors()
#    print
    the_days_that_requests_lead_to_error()
    print
    print
