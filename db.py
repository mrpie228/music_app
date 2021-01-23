

import mysql.connector

config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',
  'database': 'music',
  'raise_on_warnings': True,
}


db = mysql.connector.connect(**config)

cursor=db.cursor()

def add_new_song(name,autor,url,album):
    sql = "INSERT INTO music (name,autor,url,album) VALUES (%s, %s,%s, %s)"
    val = (name,autor,url,album)
    cursor.execute(sql,val)
    

def create_table():
    cursor.execute("CREATE TABLE music (name VARCHAR(255),autor VARCHAR(255), url VARCHAR(255),album VARCHAR(255))")

try:
    create_table()
except:
    pass

#add_new_song("говно","говно","говно","говно",)
db.commit()