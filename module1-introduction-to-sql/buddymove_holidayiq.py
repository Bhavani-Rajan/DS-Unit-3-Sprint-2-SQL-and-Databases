import sqlite3
import pandas as pd
df = pd.read_csv(`buddymove_holidayiq.csv`)
sql_conn = sqlite3.connect('rbuddymove_holidayiq.sqlite3')
sql_curs = sql_conn.cursor()
df.to_sql('review',con = sql_conn)

## - Count how many rows you have - it should be 249!

qry ='SELECT COUNT(*) FROM review;'
sql_curs.execute(qry).fetchall()

## - How many users who reviewed at least 100 `Nature` in the category also
##  reviewed at least 100 in the `Shopping` category?

qry = 'SELECT COUNT(*) FROM review WHERE Nature >= 100 AND Shopping >= 100;'
sql_curs.execute(qry).fetchall()

# 78 users reviewed at least 100 `Nature` in the category also
# reviewed at least 100 in the `Shopping` category

## - (*Stretch*) What are the average number of reviews for each category?
qry = 'SELECT AVG(Sports),AVG(Religious),AVG(Nature),AVG(Theatre),AVG(Shopping),AVG(Picnic) FROM review;'
sql_curs.execute(qry).fetchall()

# Sports  11.987
# Religious 109.779
# Nature  124.518
# Theatre 116.377
# Shopping 112.638
# Picnic 120.401
