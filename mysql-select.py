import sys
import mysql.connector
sql = """SELECT * from persons"""
try:
    #connect
    conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
    cursor = conn.cursor()
    cursor.execute(sql)
    records = cursor.fetchall()
    print(records)
    #close
    cursor.close()
    conn.close()
    print("Records retrieve sucessfully")
except:
    print("Error: ", sys.exc_info())
