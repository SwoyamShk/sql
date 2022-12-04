#import Library
import mysql.connector
import sys
sql = """UPDATE persons set name="Raj Rai", address = "BHK" WHERE pid = 1 """
try:
    # Connect
    conn = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'level4d')
    cursor = conn.cusror()
    #Update
    cursor.execute(sql)
    conn.commit()
    #Close Connection
    cursor.close()
    conn.close()
    print("Success")
except:
    print("Error",sys.exc_info())