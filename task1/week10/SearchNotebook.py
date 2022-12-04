# pip install tk
# imprt library
import sys
import tk
from tkinter import Tk #Window
from tkinter import Label #Label
from tkinter import Entry #Text Box
from tkinter import Button #Button
from notebook import NoteBook
from notebookmanager import search


def searchNoteBook():
    #reading value from entry and send to library/middleware
    nid = int(txtNID.get())
    record = search(nid)
    if(record == None):
        print("Record not found")
        txtPrice['text'] = record.getPrice()
    else:
        txtPages.delete(0, len(txtPages.get()))
        txtPages.insert(0, str(record[1]))
        txtPrice.delete(0, len(txtPrice.get()))
        txtPrice.insert(0, str(record[2]))

        # txtPages.insert(0, str(record[1]))
        # txtPrice.insert(0, str(record[2]))
        print("Record Found")

def close():
    sys.exit()




#Declare and Initialize
window = Tk()
window.geometry("250x350")
window.resizable(False,False)
window.title("Insert New Record")


lblNID = Label(window, text = "NID")
lblPages = Label(window,text= "PAGES")
lblPrice = Label(window,text= "PRICE")


txtNID = Entry(window, width = 20)
txtPages = Entry(window, width=20)
txtPrice = Entry(window, width=20)

btnSearch =Button(window, text ="Search", command= searchNoteBook)
btnClose =Button(window, text ="Close", command = close)

lblNID.place(x = 20, y = 10)
txtNID.place(x= 100, y=10)

lblPages.place(x=20, y= 40)
txtPages.place(x= 100, y =40)

lblPrice.place(x= 20, y=70)
txtPrice.place(x=100, y=70)

btnSearch.place(x=100, y=100)
btnClose.place(x=150, y=100)

window.mainloop()



