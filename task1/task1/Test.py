from driver import Driver
from ManageDriver import saveDriver
from ManageDriver import searchDriver
from ManageDriver import updateDriver
from ManageDriver import deleteDriver
from ManageDriver import allDrivers

# Test-1
# d1 = Driver() # declare and initialize object
# d1.setDID(1) # set values
# d1.setName("Aryan Rai")
# d1.setLicenseNo("BS1000091")
# saveDriver(d1) # save drive info
# values = [1, "ram", "23232"]
# updateDriver(sql, values  )


#Save
# did = name = lno = None
# did= int(input("Enter ID : "))
# name = input("NAME : ")
# lno = input("LICENSE NO : ")
# d2 = Driver(did,name,lno)
# saveDriver(d2)


#Search
# driver = searchDriver(767)
# if len(driver) == 0:
#     print("Record not Found!")
# else:
#     print(driver)


#Update

# driver2 = Driver(2, "Abhi", '7859')
# result = updateDriver(driver2)

#Delete

# result = deleteDriver(1)
# print(result)

#Update
# drivers = allDrivers()
# print(drivers)










# Update spandy
# did = name = lno = None
# did= int(input("Enter ID : "))
# name = input("NAME : ")
# lno = input("LICENSE NO : ")
# updateDriver(did, name,lno)