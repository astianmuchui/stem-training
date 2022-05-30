from webbrowser import *
from tkinter import *
root = Tk()
def myclick():
    open('http://www.instagram.com')
    
#  create a button
my_button = Button(root, text="open instagram", command=myclick, padx=20, pady=20)
my_button.pack()
root.mainloop()