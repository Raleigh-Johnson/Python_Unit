import tkinter
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

        self.sourceEntry = Entry(self.master)
        self.sourceEntry.grid(row=0,column=0,padx=(30,0),pady=(30,0))

        self.destEntry = Entry(self.master)
        self.destEntry.grid(row=0,column=1,padx=(30,0),pady=(30,0))

        self.sourceEntry = Entry(self.master)

        self.lblAdd = Label(self.master,text='Add: ', font=("Helvetica",16),fg='black',bg='beige')
        self.lblAdd.grid(row=1,column=0,padx=(30,0),pady=(30,0))

        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=lambda:self.submit)
        self.btnSubmit.grid(row=1,column=1,padx=(0,0),pady=(30,0),sticky=N+E)

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=lambda:self.cancel)
        self.btnCancel.grid(row=1,column=1,padx=(0,90),pady=(30,0),sticky=N+E)

        



        sourceEntry = askdirectory(title='Select File')
        print(sourceEntry)
"""

f = open("GenIndex.html","a")
f.write("Stay tuned for our amazing summer sale!")
f.close()
#open and read the file after the appending:
f = open("GenIndex.html","r")
print(f.read())
"""
if __name__ == "__main__":
    root = tkinter.Tk()
    app=ParentWindow(root)
    root.mainloop()
    root.withdraw()
