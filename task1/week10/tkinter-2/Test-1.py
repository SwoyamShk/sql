import tkinter
from tkinter import *

window = Tk()
window.geometry("350x350") # Resize
window.resizable(False, False) # Resizable -> False
window.title("Window1") # Title Set
#Add label

#Add Entry - Text box

lblPCPS = Label(window, text = "PCPS")

txtABC = Entry(window, width = 20)
passABC = Entry(window, show="*",width=20)
# txtDEF = Entry(window, width=20, )




radioBtn1 = Radiobutton(window, text = "Yes")
radioBtn2 = Radiobutton(window, text = "No")

check1 = Checkbutton(window, text ="Option1")
check2 = Checkbutton(window, text ="Option2")
check3 = Checkbutton(window, text ="Option3")
#
combobox1 = Listbox(window)
combobox2= Listbox(window)
combobox3 = Listbox(window)
combobox4 = Listbox(window)

# combobox['values'] = ('value1', 'value2', 'value3')

button1 = tkinter.Button(window, text="Hello")


lblPCPS.place(x = 20, y = 10)
txtABC.place(x=20, y= 70)
passABC.place(x=20,y=100)

radioBtn1.place(x=20, y= 120)
radioBtn2.place(x=20, y= 150)

check1.place(x=20, y = 180)
check2.place(x=20, y = 200)
check3.place(x=20, y = 220)

# comboBox.place(x=20, y= 240)

button1.place(x=20, y=260)




window.mainloop() # Display





























