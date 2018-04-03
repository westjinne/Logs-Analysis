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
    query_last = """
        SELECT date(log.time), cnt_error.error, cnt_total.total
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
        WHERE cnt_error.error*100/cnt_total.total >= 1
        AND date(log.time) = cnt_total.day
        AND date(log.time) = cnt_error.day
        GROUP BY date(log.time), cnt_error.error, cnt_total.total
        ORDER BY date(log.time)
    """
    last = get_data(query_last)

    for d, er, to in last:
        a = (float)(er * 100) / (float)(to)
        sys.stdout.write("%s - %.2f" % (d, a))
        sys.stdout.write("% errors")

if __name__ == '__main__':
    most_popular_three_articles()
    print
    most_popular_article_authors()
    print
    the_days_that_requests_lead_to_error()
    print
    print
