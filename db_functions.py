import sqlite3 as lite
import sys

con = lite.connect('disco.db')
cur = con.cursor()
cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
cur.execute("INSERT INTO Cars VALUES(1, 'Audi', 52642)")