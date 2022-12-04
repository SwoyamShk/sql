import mysql.connector
import sys
from driver import Driver

def saveDriver(driverInfo):
    conn = None
    sql = """INSERT INTO drivers VALUES (%s, %s, %s)"""
    values = (driverInfo.getDID(),
              driverInfo.getName(),
              driverInfo.getLicenseNo())
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
        print("Save Driver!")
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values
        del sql
        del conn

def searchDriver(licenseno):
    conn = None
    sql = """SELECT * FROM  drivers where licenseno = %s """
    values = (licenseno,)
    driver = None
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='',port="3306", database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        driver = cursor.fetchall()
        cursor.close()
        conn.close()
        print("Driver Searched")
    except:
        print("Error: ", sys.exc_info())
    finally:
        del values
        del sql
        del conn
        return driver

def updateDriver(driverInfo):
    conn = None
    sql = "UPDATE drivers SET name = %s, licenseno = %s WHERE did = %s"
    values = (driverInfo.getName(),
              driverInfo.getLicenseNo(),
              driverInfo.getDID())
    result = False
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='', port="3306", database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()#Change
        cursor.close()
        result = True
        print("Driver Updated")
    except:
        print("Error: ",sys.exc_info() )
    finally:
        del values
        del sql
        del conn
        return result

#
# def updateDriver(did,name,lno):
#     values = (did,name,lno)
#     sql = """UPDATE drivers SET Name=%s,LicenseNo=%s WHERE Did=%s"""
#     try:
#         conn = mysql.connector.connect(
#             host='localhost',
#             user='root',
#             password='',
#             port='3306',
#             database='level4d'
#         )
#         cursor = conn.cursor()
#         cursor.execute(sql,values)
#         conn.commit()
#         cursor.close()
#         conn.close()
#         print("Record Updated Successfully.")
#     except:
#         print("Error",sys.exc_info())

def deleteDriver(did):
    conn = None
    sql = """DELETE FROM drivers WHERE did=%s"""
    values = (did, )
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


def allDrivers():
    sql = """SELECT * FROM  drivers"""
    drivers = None
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
        return drivers
