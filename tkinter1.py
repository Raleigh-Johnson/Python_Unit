# Python 3.9.5
# 8/11/21


import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700,400))
        self.master.title('Learning Tkinter!')
        self.master.config(bg='beige')

        self.varFname = StringVar()
        self.varLname = StringVar()

        self.lblFname = Label(self.master,text='First Name: ', font=("Helvetica",16),fg='black',bg='beige')
        self.lblFname.grid(row=0,column=0,padx=(30,0),pady=(30,0))

        self.lblLname = Label(self.master,text='Last Name: ', font=("Helvetica",16),fg='black',bg='beige')
        self.lblLname.grid(row=1,column=0, padx=(30,0),pady=(30,0))

        self.txtFname = Entry(self.master,text =self.varFname, font=("Arial", 16),fg='black', bg='beige')
        self.txtFname.grid(row=0, column=1)

        self.txtLname = Entry(self.master,text =self.varLname, font=("Arial", 16),fg='black', bg='beige')
        self.txtLname.grid(row=1,column=1)

        self.btnSubmit = Button(self.master, text="Submit", width=20)
        self.btnSubmit.grid(row=2,column=1,padx=(0,0),pady=(30,0),Sticky=NE))
    

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
