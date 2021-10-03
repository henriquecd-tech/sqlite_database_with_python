import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

c.execute("SELECT rowid, * FROM customer ORDER BY rowid DESC")

items = c.fetchall()

for item in items:
    print(item)

print('command executed successfully...')

conn.commit()
conn.close()
