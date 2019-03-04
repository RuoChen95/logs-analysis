#!/usr/bin/python

import psycopg2

DBNAME = "news"

try:
    db = psycopg2.connect(dbname=DBNAME)
    c = db.cursor()
except Exception as e:
    print e

c.execute("""
select articles.title, count(*) as num
from articles, log
where log.path = ('/article/' || articles.slug)
group by articles.title
order by num desc limit 3
""")
results = c.fetchall()

answer1 = ""
for result in results:
    answer1 += result[0] + " -- " + str(result[1]) + " views\n"

print "What are the most popular three articles of all time?"
print answer1

c.execute("""
select authors.name, count(*) as sum
from log, articles, authors
where log.path = ('/article/' || articles.slug)
    and  articles.author = authors.id
group by name
order by sum desc
""")
results = c.fetchall()

answer2 = ""
for result in results:
    answer2 += result[0] + " -- " + str(result[1]) + " views\n"

print "Who are the most popular article authors of all time?"
print answer2

c.execute("""
select * from
(
select a.day as date, round(100 * b.hits / a.hits, 2) as errors
from
(select date(time) as day, count(*) as hits from log group by day) as a
join
(select date(time) as day, count(*) as hits from log
where status like '%404%' group by day) as b
on a.day = b.day
) as foo
where errors > 1
""")
results = c.fetchall()

answer3 = ""
for result in results:
    answer3 += str(result[0]) + " -- " + str(result[1]) + "% errors\n"

print "On which days did more than 1% of requests lead to errors?"
print answer3

db.close()
