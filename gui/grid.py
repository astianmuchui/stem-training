from tkinter import *
root = Tk()
my_label = Label(root, text="Hello World")
my_label.place(x=50, y=30)
my_label.configure(fg="#2fa4e7")
root.geometry("600x300")
root.configure(bg="gray50")
root.resizable(False, False)
root.mainloop()