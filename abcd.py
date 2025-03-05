import sqlite3 as sql

conn = sql.connect("meapp.db")

cur  = conn.cursor()
