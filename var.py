import psycopg2 as sql
from openpyxl import load_workbook
import pandas

import csv


def generate():
    with sql.connect(host='localhost',
                   user='postgres',
                   password='bunny',
                   port=5432,
                   database='deepika') as conn:
        cur = conn.cursor()
        yield (d.name for d in cur.description)
        yield from cur



"""
conn = sql.connect(host='localhost',
                   user='postgres',
                   password='bunny',
                   port=5432,
                   database='deepika')


cur = conn.cursor()


query_table = 'create table if not exists employee1(name varchar(20), salary int)'

cur.execute(query_table)
conn.commit()

cur.close()
conn.close()



data = [['name', 'age', 'salary'],
        ['bunny', 15, 25000],
        ['anil', 20, 25550]]

with open ('C:\\Users\\Deepika\\Downloads\\output.csv', mode='r', newline='',) as file:
    reader = csv.DictReader(file)
    for i in reader:
        print(i)"""
    



   
