import pymysql

def create_conn():
#    conn = sql.connect("host='kermit' user='dmontysql' passwd='sun37rIse' db='pyBase'")
        conn = pymysql.connect("host='us1604' user='dmontysql' passwd='37sunrIse' db='pyBase'")
        return conn
 
def create_table():
    conn = create_conn()
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = create_conn()
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()
    
def view():
    conn = create_conn()
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = create_conn()
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item = ?", (item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn = create_conn()
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity = ?, price = ? WHERE item = ?", (item, quantity, price))
    conn.commit()
    conn.close()


create_table()
print(view())    