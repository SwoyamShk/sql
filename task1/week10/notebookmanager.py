import sys
import mysql.connector

def connect():
    conn = None
    try:
        conn = mysql.connector.connect(
            host = 'localhost',
            port = '3306',
            user = 'root',
            password = '',
            database = 'level4d'
        )
    except:
        print("Error: ",sys.exc_info())
    finally:
        return conn

def insert(notebook):
    conn = None
    sql = """INSERT INTO notebooks VALUES(%s, %s, %s)"""
    values = (notebook.getNID(),
              notebook.getPages(),
              notebook.getPrice())
    record = False
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql,values)
        conn.commit()
        cursor.close()
        conn.close()
        result = True
    except:
        print("Error: ",sys.exc_info())
    finally:
        del values
        del sql
        del conn
        return record

def all():
    sql = """SELECT * FROM notebooks"""
    record = None

    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='', port="3306", database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql)
        record = cursor.fetchall()
        print(record)
        cursor.close()
        conn.close()
        print("All Drivers Displayed")
    except:
        print("Error: ", sys.exc_info())
    finally:
        del sql
        return record

def search(nid):
    sql = """SELECT * FROM notebooks WHERE nid = %s"""
    values = (nid,)
    record = None
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='', port="3306", database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        record = cursor.fetchone()
        cursor.close()
        conn.close()
        print("Notebook Searched")
    except:
        print("Error: ", sys.exc_info())
    finally:
        del values, conn
        return record

def edit(notebook):
    sql = """UPDATE notebooks set pages= %s, price = %s WHERE nid = %s"""
    values = (notebook.getPages(), notebook.getPrice(), notebook.getNID())
    record = False
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        record = True
    except:
        print("Error: ",sys.exc_info())
    finally:
        del values, sql
        return record

def delete(nid):
    conn = None
    sql = """DELETE FROM notebooks WHERE nid=%s"""
    values = (nid,)
    record = False
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='', port="3306", database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        record = True
    except:
        print("Error: ", sys.exc_info())
    finally:
        del values
        del sql
        del conn
        return record