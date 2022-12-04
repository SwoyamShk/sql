# pip install tk

from tkinter import Tk

window = Tk() # declare and initialize
window.geometry("450x450") # Resize
window.resizable(False, False) # Resizable -> False
window.title("Main Window") # Title Set
window.mainloop() # Display