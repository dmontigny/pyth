import mysql.connector
from mysql.connector import errorcode

db='pyBase'

def create_conn():
    config = {
        'user':'dmontysql',
        'password':'37Sunrise',
#        'password':'sun37rIse',
        'host':'us1604',
#        'host':'kermit',
        'db':'pyBase',
        'raise_on_warnings': True,
    } 
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return
    else:
        return cnx

TABLES = {} 

#TABLES['store'] = ("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
TABLES['store'] = (
    "CREATE TABLE `store` ("
    "  `item` VARCHAR(50) NOT NULL,"
    "  `quantity` INT(11) NOT NULL,"
    "  `price` FLOAT NOT NULL" 
    ") ENGINE=InnoDB")

def create_tables():
    conn = create_conn()
    cur=conn.cursor()
    for name, ddl in TABLES.items():
        try:
            print("Creating table {}: ".format(name), end='')
            cur.execute(ddl)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")
    
    cur.close()
    conn.close()

def insert(item, quantity, price):
    conn = create_conn()
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quantity, price))
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
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn = create_conn()
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity = %s, price = %s WHERE item = %s", (item, quantity, price))
    conn.commit()
    conn.close()

insert('orange', 23, 2.75)
create_tables()
print(view())    