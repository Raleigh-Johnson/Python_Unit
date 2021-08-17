from tkinter import filedialog
import tkinter
from tkinter import *
import os 
import socket
import shutil
import sys



class ParentWindow(Frame):      
    def __init__ (self, master):
        Frame.__init__ (self,master)




        self.EntryIN = Entry(master)
        self.EntryIN.grid(row=1, column=3)
        
        self.EntryOut = Entry(master)
        self.EntryOut.grid(row=2, column=3)
        


        self.buttonIN = Button( master, text="Get Source",command=lambda:self.browse())
        self.buttonIN.grid(row=1,column=0, sticky = W)
        

        self.buttonOut = Button( master, text="Destination",command=lambda:self.dest())
        self.buttonOut.grid(row=2,column=0, sticky = W)

        self.buttonClose = Button(master, text = "Close",command=lambda:self.buttonClose())
        self.buttonClose.grid(row=3,column=1, sticky = E)

        self.buttonUpload = Button(master, text = "Transfer",command=lambda:self.FileTransfer())
        self.buttonUpload.grid(row=3,column=2, sticky = E)

    def browse(self): #User Chooses source
        filename = filedialog.askdirectory()
        self.EntryIN.insert(0,filename)

    def dest(self): #User Chooses destination
        filename = filedialog.askdirectory()
        self.EntryOut.insert(0,filename)
        


    def FileTransfer(self):
        #Gets text from the EntryIN Widget and saves it to a var named "source"
        source=self.EntryIN.get()
        #Gets destination path for EntryOut Widget and saves it to a var named "Dest"
        Dest=self.EntryOut.get()
        #Creates a list of files in the source path and saves it to a variable named "Files"
        Files=os.listdir(source)
        #iterates through list of files 
        for item in Files:
            #Concatenates the source path with the file name
            fullPath=source+"/"+item
            #Transfers File at the specified path to the destinatation Folder
            shutil.move(fullPath,Dest)
            
    def buttonClose(self):
        sys.exit()
            
         
        
    

        
    
    

    
        
   


if __name__ == "__main__":
    root = tkinter.Tk()
    app= ParentWindow(root)
    root.mainloop()
