from tkinter import *
from tkinter import messagebox
class Calculator():
    def __init__(self, parent):
        self.parent = parent
        self.create_widgets()
        
    def backspace(self):
            self.entr_lbl.delete(len(self.entr_lbl.get())-1)
            
    def clear(self):
        self.entr_lbl.delete(0,END)
        
    def put_one(self):
        self.entr_lbl.insert(END,"1")
        
    def put_two(self):
        self.entr_lbl.insert(END,"2")
        
    def put_three(self):
        self.entr_lbl.insert(END,"3")
        
    def put_four(self):
        self.entr_lbl.insert(END,"4")
    def put_five(self):
        self.entr_lbl.insert(END,"5")
    def put_six(self):
        self.entr_lbl.insert(END,"6")
    def put_seven(self):
        self.entr_lbl.insert(END,"7")
    def put_eight(self):
        self.entr_lbl.insert(END,"8")
    def put_nine(self):
        self.entr_lbl.insert(END,"9")
    def put_zero(self):
        self.entr_lbl.insert(END,"0")
    def put_decimal(self):
        self.entr_lbl.insert(END,".")
    def put_plus(self):
        self.entr_lbl.insert(END,"+")
    def put_minus(self):
        self.entr_lbl.insert(END,"-")
    def put_multiply(self):
        self.entr_lbl.insert(END,"x")
    def put_divide(self):
        self.entr_lbl.insert(END,"÷")
    def put_percent(self):
        self.entr_lbl.insert(END,"%")                                                                
    def calculate(self):
        try:
            if self.entr_lbl.get() == "":
                messagebox.showerror("Error","Please enter a value")
            else:
                self.string = self.entr_lbl.get()
                if '+' in self.string:
                        #addition
                    self.num = self.string.index('+')
                    self.fnum = self.string[:self.num].strip()
                    self.snum = self.string[self.num+1:].strip()
                    self.entr_lbl.delete(0,END)
                    self.entr_lbl.insert(0,float(self.fnum)+float(self.snum))
                elif '-' in self.string:
                    #subtraction
                    self.num = self.string.index('-')
                    self.fnum = self.string[:self.num].strip()
                    self.snum = self.string[self.num+1:].strip()
                    self.entr_lbl.delete(0,END)
                    self.entr_lbl.insert(0,float(self.fnum)-float(self.snum))
                elif 'x' in self.string:
                    #multiplication
                    self.num = self.string.index('x')
                    self.fnum = self.string[:self.num].strip()
                    self.snum = self.string[self.num+1:].strip()
                
                    self.entr_lbl.delete(0,END)
                    self.entr_lbl.insert(0,float(self.fnum)*float(self.snum))        
                elif '÷' in self.string:
                    #division
                    self.num = self.string.index('÷')
                    self.fnum = self.string[:self.num].strip()
                    self.snum = self.string[self.num+1:].strip()
                    self.entr_lbl.delete(0,END)
                    self.entr_lbl.insert(0,float(self.fnum)/float(self.snum))    
                elif '%' in self.string:
                    #modulus
                    self.num = self.string.index('%')
                    self.fnum = self.string[:self.num].strip()
                    self.snum = self.string[self.num+1:].strip()
                    self.entr_lbl.delete(0,END)
                    self.entr_lbl.insert(0,float(self.fnum)%float(self.snum))
                else:
                    messagebox.showerror("Error","Please enter a valid expression")    
        except ValueError:
            messagebox.showerror("Error","Please enter a valid value")
        except ZeroDivisionError:
            messagebox.showerror("Error","Zero division error")    
    def create_widgets(self):
         self.welcm_lbl = Label(self.parent, text="Standard",fg="#2fa4e7", font=("bold" ,15),bg="#00030a",padx=10)
         self.welcm_lbl.place(x=10,y=10)
         
         self.entr_lbl = Entry(self.parent,fg="#2fa4e7",bg="#00030a",font=("bold",30))
        #  self.entr_lbl.insert(0,"0")
         self.entr_lbl.place(x=20,y=65,height=130,width=500)    
            
         # create buttons 
         
         self.mod_btn = Button(self.parent,text="%",padx=20,pady=20,font=("bold",12),bg="#00040a",fg="#2fa4e7",activebackground="#00030a" ,command=self.put_percent)
         self.mod_btn.place(x=20,y=220)
         
         self.add_btn = Button(self.parent,text="+",command=self.put_plus,padx=20,pady=20,font=("bold",12),bg="#00040a",fg="#2fa4e7",activebackground="#00030a")
         self.add_btn.place(x=90,y=220)
         
         self.sub_btn = Button(self.parent,text="-",padx=20,pady=20,command=self.put_minus,font=("bold",12),bg="#00040a",fg="#2fa4e7",activebackground="#00030a")
         self.sub_btn.place(x=155,y=220)   
         
         self.mul_btn = Button(self.parent,text="x",command=self.put_multiply,padx=20,pady=20,font=("bold",12),bg="#00040a",fg="#2fa4e7",activebackground="#00030a")
         self.mul_btn.place(x=215,y=220)
         
         self.div_btn = Button(self.parent,text="÷",command=self.put_divide,padx=20,pady=20,font=("bold",12),bg="#00040a",fg="#2fa4e7",activebackground="#00030a")
         self.div_btn.place(x=215,y=295)
         
         self.clear_btn = Button(self.parent,text="C",command=self.clear,padx=20,pady=20,font=("bold",12),bg="#00030a",fg="#2fa4e7",activebackground="#00030a")
         self.clear_btn.place(x=215,y=220)
         
         self.backspace_btn = Button(self.parent,text="<",padx=20,pady=20,command=self.backspace,font=("bold",12),bg="#00030a",fg="#2fa4e7",activebackground="#00030a")
         self.backspace_btn.place(x=215,y=370)
         
         self.nine = Button(self.parent,text="7",padx=20,pady=20,command=self.put_seven,font=("bold",12),bg="#2fa4e7",fg="#00030a",activebackground="#2fa4e7")
         self.nine.place(x=20,y=295)
         
         self.eight = Button(self.parent,text="8",command=self.put_eight,padx=20,pady=20,font=("bold",12),bg="#2fa4e7",fg="#00030a",activebackground="#2fa4e7")
         self.eight.place(x=85,y=295)
         
         self.seven = Button(self.parent,text="9",command=self.put_nine,padx=20,pady=20,font=("bold",12),bg="#2fa4e7",fg="#00030a",activebackground="#2fa4e7")
         self.seven.place(x=150,y=295)
         
         self.six = Button(self.parent,text="4",command=self.put_four,padx=20,pady=20,font=("bold",12),bg="#2fa4e7",fg="#00030a",activebackground="#2fa4e7")
         self.six.place(x=20,y=370)
         
         self.five = Button(self.parent,text="5",command=self.put_five,padx=20,pady=20,font=("bold",12),bg="#2fa4e7",fg="#00030a",activebackground="#2fa4e7")
         self.five.place(x=85,y=370)
         
         self.four = Button(self.parent,text="6",padx=20,command=self.put_six,pady=20,font=("bold",12),bg="#2fa4e7",fg="#00030a",activebackground="#2fa4e7")
         self.four.place(x=150,y=370)
         
         self.three = Button(self.parent,text="1",padx=20,command=self.put_one,pady=20,font=("bold",12),bg="#2fa4e7",fg="#00030a",activebackground="#2fa4e7")
         self.three.place(x=20,y=450)
         
         self.two = Button(self.parent,text="2",command=self.put_two,padx=20,pady=20,font=("bold",12),bg="#2fa4e7",fg="#00030a",activebackground="#2fa4e7")
         self.two.place(x=85,y=450)
         
         self.one = Button(self.parent,text="3",command=self.put_three,padx=20,pady=20,font=("bold",12),bg="#2fa4e7",fg="#00030a",activebackground="#2fa4e7")
         self.one.place(x=150,y=450)
         
         self.zero = Button(self.parent,text="0",command=self.put_zero,padx=20,pady=20,font=("bold",12),bg="#2fa4e7",fg="#00030a",activebackground="#2fa4e7")
         self.zero.place(x=215,y=450)
         
         self.decimal_btn = Button(self.parent,text=".",command=self.put_decimal,padx=20,pady=20,font=("bold",12),bg="#2fa4e7",fg="#00030a",activebackground="#2fa4e7")
         self.decimal_btn.place(x=278,y=450)
         
         self.equals = Button(self.parent,text="=",command=self.calculate,padx=30,pady=20,font=("bold",12),bg="#2fa4e7",fg="#00030a",activebackground="#2fa4e7")
         self.equals.place(x=340,y=450)
         
         

         
         
             
             
if __name__ == '__main__':
    app = Tk()
    app.geometry("600x600")
    app.title("Calculator App")
    app.resizable(False,False)
    app.configure(bg="#00030a")
    root  = Calculator(app)
    app.mainloop() 