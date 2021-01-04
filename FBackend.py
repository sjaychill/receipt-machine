import sqlite3


def creat():
    conn = sqlite3.connect("Store2.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Store2s(id INTEGER PRIMARY KEY,Item TEXT,Quantity INTEGER,tax TEXT,Price TEXT)")
    conn.commit()
    conn.close()


creat()


def Insert(Item, Quantity, tax, Price):
    conn = sqlite3.connect("Store2.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO Store2s VALUES (NULL,?,?,?,?)",
                (Item, Quantity, tax, Price))
    conn.commit()
    conn.close()


def Search(Item="", Quantity="", tax="", Price=""):
    conn = sqlite3.connect("Store2.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Store2s WHERE Item=? OR Quantity=? OR tax=? OR Price=?",
                (Item, Quantity, tax, Price))
    rows = cur.fetchall()
    conn.close()
    return rows


def view():
    conn = sqlite3.connect("Store2.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Store2s ")
    row = cur.fetchall()
    conn.close()
    return row

    print("RECEIPT".center(20, '-'))
    for i in view():
        print(i)


def Delete(Item,):
    con = sqlite3.connect("Store2.db")
    cur = con.cursor()
    cur.execute("DELETE FROM Store2s WHERE Item=?", (Item,))
    rows = cur.fetchall()
    con.close()
