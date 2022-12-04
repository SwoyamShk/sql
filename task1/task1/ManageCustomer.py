import mysql.connector
import sys
from customer import Customer

def saveCustomer(customerInfo):
    conn = None
    sql = """INSERT INTO customers VALUES (%s, %s, %s, %s, %s)"""
    values = (customerInfo.getCID(),
              customerInfo.getName(),
              customerInfo.getAddress(),
              customerInfo.getEmail(),
              customerInfo.getMobile())
    try:
        conn = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='',
            database='level4d'
        )
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        print("Customer Saved!")
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values
        del sql
        del conn

def searchCustomer(mobile):
    conn = None
    sql = """SELECT * FROM  customers where mobile = %s """
    values = (mobile,)
    customer = None
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='',port="3306", database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        driver = cursor.fetchall()
        cursor.close()
        conn.close()
        print("Customer Searched")
    except:
        print("Error: ", sys.exc_info())
    finally:
        del values
        del sql
        del conn
        return customer

def updateCustomer(customerInfo):
    conn = None
    sql = "UPDATE customers SET name = %s, address = %s, email = %s, mobile= %s WHERE cid = %s"
    values = (customerInfo.getName(),
              customerInfo.getAddress(),
              customerInfo.getEmail(),
              customerInfo.getMobile(),
              customerInfo.getCID())
    result = False
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='', port="3306", database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()#Change
        cursor.close()
        result = True
        print("Customer Updated")
    except:
        print("Error: ",sys.exc_info() )
    finally:
        del values
        del sql
        del conn
        return result

def deleteCustomer(cid):
    conn = None
    sql = """DELETE FROM customers WHERE cid=%s"""
    values = (cid, )
    result = False
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='',port="3306", database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result = True
    except:
        print("Error: ", sys.exc_info())
    finally:
        del values
        del sql
        del conn
        return result


def allCustomer():
    sql = """SELECT * FROM  customers"""
    customers = None
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='', port="3306", database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql)
        drivers = cursor.fetchall()
        print(drivers)
        cursor.close()
        conn.close()
        print("All Drivers Displayed")
    except:
        print("Error: ", sys.exc_info())
    finally:
        del sql
        del conn
        return customers
