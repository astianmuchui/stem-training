from tkinter import * 
root = Tk()
# create a  function to get input 
def myclick():
    my_label = Label(root, text="Hey you clicked me")
    my_label.pack()
my_button = Button(root, text="click me",command=myclick,fg="#2fa4e7", bg="#00030a")
my_button.pack()

root.mainloop()