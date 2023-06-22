"""

import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(
    dbname="recommender_test",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

create_table_query = '''
CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    hire_date DATE
)
'''

cur.execute(create_table_query)
conn.commit()

insert_query = '''
INSERT INTO employees (first_name, last_name, hire_date)
VALUES (%s, %s, %s)
'''
select_query = '''
SELECT * FROM employees;
'''

data = ('John', 'Doe', '2023-06-17')

result = cur.execute(insert_query, data)
conn.commit()

cur.execute(select_query, data)
conn.commit()


rows = cur.fetchall()
for row in rows:
    print(row)


cur.close()
conn.close()
"""