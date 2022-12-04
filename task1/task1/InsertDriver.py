# pip install tk
# import library

from tkinter import Tk #Window
from tkinter import Label #Label
from tkinter import Entry #Text Box
from tkinter import Button #Button
from driver import Driver
from ManageDriver import saveDriver


def save():
    #reading value from entry and send to library/middleware
    did = int(txtDID.get())
    name = txtName.get()
    lno = txtLicenseNo.get()
    nb1 = Driver(did, name, lno)
    result = saveDriver(nb1)
    if(result == True):
        print("Insert Sucessfully")
    else:
        print("Error to insert")

#Declare and Initialize
window = Tk()
window.geometry("250x350")
window.resizable(False,False)
window.title("Insert New Driver")


lblDID = Label(window, text = "DID")
lblName = Label(window,text= "NAME")
lblLicenseNo = Label(window,text= "LICENSENO")


txtDID = Entry(window, width = 20)
txtName = Entry(window, width=20)
txtLicenseNo = Entry(window, width=20)

btnSave =Button(window, text ="Save", command= save)
btnClose =Button(window, text ="Close")

lblDID.place(x = 20, y = 10)
txtDID.place(x= 100, y=10)

lblName.place(x=20, y= 40)
txtName.place(x= 100, y =40)

lblLicenseNo.place(x= 20, y=70)
txtLicenseNo.place(x=100, y=70)

btnSave.place(x=100, y=100)
btnClose.place(x=150, y=100)

window.mainloop()