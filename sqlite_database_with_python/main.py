import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

c.execute("DROP TABLE customer")
conn.commit()

c.execute("SELECT rowid, * FROM customer LIMIT 4")

items = c.fetchall()

for item in items:
    print(item)

print('command executed successfully...')

conn.commit()
conn.close()
