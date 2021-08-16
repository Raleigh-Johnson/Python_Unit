import tkinter
import webPageGenerator
import WebPageFunction
from tkinter import *
from tkinter.filedialog import askdirectory



class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self,master)
        

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700,400))
        self.master.title('Add to HTML')
        self.master.config(bg='beige')

        self.txtBody = Entry(self.master)
        self.txtBody.grid(row=0,column=0,padx=(30,0),pady=(30,0))

        self.sourceEntry = Entry(self.master)

        #Add Lable above text box that reads "Add Text to be added to HTML file."
        """self.btnAdd = Button(self.master,text='OpenWebpage',command=lambda:WebPageFunction.createFile(self), font=("Helvetica",16),fg='black',bg='beige')
        self.btnAdd.grid(row=1,column=0,padx=(10,0),pady=(30,0))"""
        
        self.btncreate = Button(self.master,text='Add Text',command=lambda:WebPageFunction.newBody(self), font=("Helvetica",16),fg='black',bg='beige')
        self.btncreate.grid(row=2,column=0,padx=(10,0),pady=(30,0))

        self.btnWebpage = Button(self.master, text="Open Webpage", width=10, height=2, command=lambda:WebPageFunction.Webpage(self))
        self.btnWebpage.grid(row=1,column=1,padx=(0,0),pady=(30,0),sticky=N+E)


if __name__ == "__main__":
    root = tkinter.Tk()
    app=ParentWindow(root)
    root.mainloop()
    root.withdraw()
