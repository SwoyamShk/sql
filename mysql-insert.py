import sys
import mysql.connector
sql = """INSERT INTO persons VAlUES(1, 'Swoyam Shakya', 'Patan')"""
try:
    conn = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'level4d')
    #insert
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    # close
    cursor.close()
    conn.close()
    print("Insert record sucessfully")
except:
    print("Error: ",sys.exc_info())
