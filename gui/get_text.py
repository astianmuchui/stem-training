from tkinter import * 
root = Tk()
root.configure(bg="#00030a")
# create a  function to get input 
e = Entry(root,width=50,fg="#2fa4e7", bg="#00030a")
e.pack()

f = Entry(root,width=50,fg="#2fa4e7", bg="#00030a")
f.pack()

# create placeholder


def myclick():
    f_num = float(e.get())
    s_num = float(f.get())
    
    sum = "Sum : "+str(f_num + s_num)
    sub = "Difference : "+str(f_num- s_num)
    div = "Division : "+str(f_num/s_num )
    mult = "Product : "+str(f_num*s_num)
    ls = [sum,sub,div,mult]
    for s in ls:        
        my_label = Label(root, text=s)
        my_label.configure(bg="#00030a",fg="#2fa4e7")   
        my_label.pack()
        e.delete(0,END)
        f.delete(0,END)
my_button = Button(root, text="calculate",command=myclick,fg="#2fa4e7", bg="#00030a")
my_button.pack()

# Tkinter entry

root.mainloop()