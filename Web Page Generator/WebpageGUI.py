import tkinter
import WebPageFunction
from tkinter import *
from tkinter.filedialog import askdirectory


# Run Command from here.
class ParentWindow(Frame):      
    def __init__ (self, master):
        Frame.__init__ (self,master)
        

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700,400))
        self.master.title('Add to HTML')
        self.master.config(bg='beige')

        self.sourceEntry = Entry(self.master)

        #Label to add text 
        self.lblAddText = Label(self.master,text='Enter Text: ', font=("Helvetica",16),fg='black',bg='beige')
        self.lblAddText.grid(row=0,column=0, padx=(5,0),pady=(10,0),sticky = W )
        #Text body to add custome text 
        self.txtBody = Entry(self.master)
        self.txtBody.grid(row=1,column=0,padx=(5,0),pady=(0,0),sticky = W)
        #Opens file with selected custome text
        self.btncreate = Button(self.master,text='Open Webpage',command=lambda:WebPageFunction.newBody(self), font=("Helvetica",16),fg='black',bg='beige')
        self.btncreate.grid(row=2,column=0,padx=(5,0),pady=(20,0),sticky = W)

if __name__ == "__main__":
    root = tkinter.Tk()
    app=ParentWindow(root)
    root.mainloop()
    root.withdraw()
