import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

c.execute("DELETE from customer WHERE first_name = 'Dan'")

conn.commit()

c.execute("SELECT rowid, * FROM customer")

items = c.fetchall()

for item in items:
    print(item)

print('command executed successfully...')

conn.commit()

conn.close()
