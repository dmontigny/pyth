import mysql.connector
from mysql.connector import errorcode

def create_conn():
    config = {
        'user':'dmontysql',
        'password':'37Sunrise',
        'host':'us1604',
#        'password':'sun37rIse',
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
#    conn = pymysql.connect("host='us1604' user='dmontysql' passwd='37sunrIse' db='pyBase'")
#   return conn

db='pyBase'
TABLES = {} 

#TABLES['store'] = ("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
TABLES['titles'] = (
    "CREATE TABLE `books` ("
    "  `idtitle` INT(11) NOT NULL AUTO_INCREMENT,"
    "  `title` VARCHAR(75),"
    "  `author` VARCHAR(25) NOT NULL,"
    "  `year` INT(11),"
    "  `ISBN` INT(11),"
    "  PRIMARY KEY (`idtitle`)" 
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

def insert(title, author, year, isbn):
    conn = create_conn()
    cur=conn.cursor()
    cur.execute("INSERT INTO books (title, author, year, isbn)"
                " VALUES(%s,%s,%s,%s)", (title, author, year, isbn))
    conn.commit()
    conn.close()
    
def view():
    conn = create_conn()
    cur=conn.cursor()
    cur.execute("SELECT * FROM books")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", year="", isbn=""):
    conn = create_conn()
    cur=conn.cursor()
    cur.execute("SELECT * FROM books WHERE title=%s OR author=%s OR year=%s OR isbn =%s", (title, author, year, isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = create_conn()
    cur=conn.cursor()
    cur.execute("DELETE FROM books WHERE item=%s", (item,))
    conn.commit()
    conn.close()

def update(idtitle, title, author, year, isbn):
    conn = create_conn()
    cur=conn.cursor()
    print("UPDATE books SET title = %s, author = %s, year = %s, isbn = %s WHERE idtitle = %s " % (title, author, year, isbn, idtitle))
    try:
        cur.execute("UPDATE books SET title = %s, author = %s, year = %s, isbn = %s WHERE idtitle = %s", (title, author, year, isbn, idtitle))
    except mysql.connector.Error as err:
        print(err, err.errno)
    else:
        print("OK")
    conn.commit()
    conn.close()

#insert('orange', 23, 2.75)
print(search("The Hobbit", "J.R.R. Tolkein", 1940, 123456))
#print(search("The Hobbit"))
update(1, "The Hobbit", "J.R.R. Tolkein", 1940, 123456)
print(view())
