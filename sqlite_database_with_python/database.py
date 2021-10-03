import sqlite3


# query the db and return all records
def show_all():
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM customer")
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()
