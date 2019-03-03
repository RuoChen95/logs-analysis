import psycopg2

DBNAME = "news"


def get_data():
	db = psycopg2.connect(dbname=DBNAME)
	c = db.cursor()
	c.execute("""
		select articles.title, logs.path, logs.num
		from articles, (select path, count(*) as num from log group by path order by num desc) as logs
		where logs.path = ('/article/' || articles.slug) limit 3
		""")
	results = c.fetchall()
	
	answer1 = ""
	for result in results:
		answer1 += result[0] + " -- " + str(result[2]) + " views\n"
		
	print answer1
	
	c.execute("""
		select logs.name, count(*) as sum
		from
		(select log.path, log.time, articles.author, articles.slug, authors.id, authors.name
		from log, articles, authors
		where log.path = ('/article/' || articles.slug) and  articles.author = authors.id) as logs
		group by logs.name
		order by sum desc
		""")
	results = c.fetchall()
	
	answer2 = ""
	for result in results:
		answer2 += result[0] + " -- " + str(result[1]) + " views\n"
	
	print answer2
	
	c.execute("""
		select * from
		(
    select a.day as date, round(100 * cast((b.hits) as decimal) / cast(a.hits + b.hits as decimal), 2) as errors
    from
    (select date(time) as day, count(*) as hits from log group by day) as a
    join
    (select date(time) as day, count(*) as hits from log where status like '%404%' group by day) as b
    on a.day = b.day
    ) as foo
    where errors > 1
		""")
	results = c.fetchall()
	
	answer3 = ""
	for result in results:
		answer3 += str(result[0]) + " -- " + str(result[1]) + "% errors\n"
	
	print answer3

	db.close()


get_data()