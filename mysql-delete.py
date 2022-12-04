#import Library
import mysql.connector
import sys
sql = """DELETE FROM persons WHERE pid = 1"""
try:
    # Connect
    conn = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'level4d')
    cursor = conn.cursor()
    #Delete
    cursor.execute(sql)
    conn.commit()
    #Close Connection
    cursor.close()
    conn.close()
    print("Success")
except:
    print("Error",sys.exc_info())
