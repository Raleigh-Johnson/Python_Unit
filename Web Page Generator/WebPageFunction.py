import os
import webbrowser
from tkinter import *
import webPageGenerator
import WebpageGUI

def createFile(self):
    f = open("GenIndex.html","w")
    f.write("Stay tuned for our amazing summer sale!")
    #open and read the file after the appending:
    f = open("GenIndex.html","r")
    print(f.read())
    f.close()

def newBody(self):
    f = open("GenIndex.html","w")
    body =""" <html><body>{}</body></html> """.format(self.txtBody.get())
    f.write(body)
    f = open("GenIndex.html","r")
    f.close()
    

    
