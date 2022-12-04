# pip install tk
# imprt library
import sys
import tk
from tkinter import Tk #Window
from tkinter import Label #Label
from tkinter import Entry #Text Box
from tkinter import Button #Button
from notebook import NoteBook
from notebookmanager import edit, delete, search


def deleteNoteBook():
    #reading value from entry and send to library/middleware
    nid = int(txtNID.get())
    # pages = int(txtPages.get())
    # price = float(txtPrice.get())
    record = delete(nid)
    if(record == True):
        print("Notebook Deleted")
        # txtPrice['text'] = record.getPrice()
    else:
        # txtPages.insert(0, str(record[1]))
        # txtPrice.insert(0, str(record[2]))
        print("Notebook not Deleted")

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

# def editNoteBook():
#     pass
#     #read all values(nid, page, and price)
#     nid = int(txtNID.get())
#     pages = int(txtPages.get())
#     price = float(txtPrice.get())
#     #create NoteBook object and initialize
#     nb1 = NoteBook(nid, pages, price)
#     #send and edit
#     result = edit(nb1)
#     if result == True:
#         print("Record Edited")
#     else:
#         print("Error to Edit")
def close():
    sys.exit()




#Declare and Initialize
window = Tk()
window.geometry("250x350")
window.resizable(False,False)
window.title("Delete Existing Record")


lblNID = Label(window, text = "NID")
lblPages = Label(window,text= "PAGES")
lblPrice = Label(window,text= "PRICE")


txtNID = Entry(window, width = 20)
txtPages = Entry(window, width=20)
txtPrice = Entry(window, width=20)

btnSearch =Button(window, text ="Search", command= searchNoteBook)
btnDelete =Button(window, text ="Delete", command = deleteNoteBook)

lblNID.place(x = 20, y = 10)
txtNID.place(x= 100, y=10)

lblPages.place(x=20, y= 40)
txtPages.place(x= 100, y =40)

lblPrice.place(x= 20, y=70)
txtPrice.place(x=100, y=70)

btnSearch.place(x=100, y=100)
btnDelete.place(x=150, y=100)

window.mainloop()



