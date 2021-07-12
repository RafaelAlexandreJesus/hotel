import pymysql.cursors

def conectar():
    conn = pymysql.connect(
      host='localhost',
        user='root',
        password='',
        database='escola',
        cursorclass=pymysql.cursors.DictCursor  
    )
    return conn