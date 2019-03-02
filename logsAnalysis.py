import psycopg2

DBNAME = "news"


def get_data():
	db = psycopg2.connect(dbname=DBNAME)
	c = db.cursor()
	c.execute("select articles.title, logs.path, logs.num from articles, (select path, count(*) as num from log group by path order by num desc limit 5 offset 1) as logs where logs.path = ('/article/' + articles.slug)")
	results = c.fetchall()
	print results
	db.close()


get_data()