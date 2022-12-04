import sys
import mysql.connector

def insertRecord(userInfo):
    conn = None
    sql = """INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s)"""
    try:
        conn = mysql.connector.connect(host = "localhost", user = "root", password = "", port = '3306', database = "level4d")
        cursor = conn.cursor()
        cursor.execute(sql, userInfo)
        conn.commit()
        conn.close()
        cursor.close()
        print("Record Inserted")
    except:
        print("Error: ", sys.exc_info())
    finally:
        del conn
        del sql

def loginUser(userInfo):
    conn = None
    sql = """SELECT * FROM users WHERE email=%s and password=%s"""
    try:
        conn = mysql.connector.connect()
        cursor = conn.cursor()
        cursor.execute(sql, userInfo)
        user = cursor.fetchall()
        print(user)
        if user!= None:
            print("Welcome", user[0][1])
        else:
            print("User not found!")
        cursor.close()
        conn.close()
    except:
        print("Error: ", sys.exc_info())
    finally:
        del sql
        del conn

#TEST

# userInfo = (2, 'Baj Rai', 'KTM', 'baj@mail.com', '12345', '9876532351')
# insertRecord(userInfo)

userInfo = ('raj@mail.com', '12345') #[0, 1]
loginUser(userInfo)

