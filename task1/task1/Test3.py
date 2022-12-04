from trip import Trip
from ManageTrip import saveTripInfo

#Save
pick = drop = time = date =None
pick= input("Enter PickIp Address : ")
drop = input("Enter DropOff Address : ")
time = input("Enter PickUp Time : ")
date = input("Enter PickUp Date : ")

t2 = Trip(pick, drop, time, date)
saveTripInfo(t2)