#Display a window with a button
import tkinter
from tkinter import *
from tkinter import ttk #ComboBox
from PIL import ImageTk, Image

class Window2():
    def __init__(self):
        window = Tk()
        window.title("Window-2")
        window.resizable(False,False)
        window.geometry("350x450")


        #Add Label
        lblCollege = Label(window, text = "PCPS College")
        lblCollege.place(x=20, y = 20)

        # Add Entry - text box - single line
        txtName = Entry(window,width=20)
        txtName.place(x = 20, y = 50)

        #Add password box
        txtPass = Entry(window,width = 20, show= '*')
        txtPass.place(x=20, y= 80)

        #Text - Comment box/Text area
        txtComments = Text(window, width=30, height=3)
        txtComments.place(x=20, y=140)

        rb1 = Radiobutton(window, text="Option-1", value='v1')
        rb2 = Radiobutton(window, text="Option-2", value='v2')

        rb1.place(x=20, y= 170)
        rb2.place(x=20, y=200)

        #Checkbutton - CheckBox( Select multiple option

        ck1 = Checkbutton(window, text="Option-1")
        ck2 = Checkbutton(window, text="Option-2")
        ck3 = Checkbutton(window, text="Option-3")

        ck1.place(x=20, y=230)
        ck2.place(x=20, y=260)
        ck3.place(x=20, y=290)

        cmb1 = ttk.Combobox(window)
        cmb1['values'] = ('Value-1', 'Values-2', 'Values-3')
        cmb1.place(x=20, y= 320)

        #Canvas - Image Viewer
        #pip install pillow
        #from PIL import ImageTk, Image
        #
        # tmpImage = Image.open('Untitled.png')
        # imgFile = ImageTk.PhotoImage(tmpImage)

        #Button
        btnSave = Button(window, text="SAVE")
        btnSave.place(x=20, y=380)






        window.mainloop()


