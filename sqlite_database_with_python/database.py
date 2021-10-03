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


# add new record to the table
def add_one(first, last, email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customer VALUES(?,?,?)", first, last, email)
    conn.commit()
    conn.close()


# delete record from table
def delet_one(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE from customer WHERE rowid = (?)", id)
    conn.commit()
    conn.close()


# add many records to table
def add_many(list):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customer VALUES (?, ?, ?)", list)
    conn.commit()
    conn.close()


def email_lookup(email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT * from customer WHERE email = (?)", (email,))
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()
