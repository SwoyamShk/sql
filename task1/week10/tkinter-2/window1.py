#Display a window with a button

from tkinter import *
from window2 import Window2

def displayWin():
    Window2() # Call __init__() function

window = Tk()
btn1 = Button(window, text="Window", command=Window2)
btn1.place(x=20, y=20)

window.geometry("350x350")
window.resizable(False, False)
window.title("Window1")


window.mainloop()