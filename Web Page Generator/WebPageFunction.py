import os
import webbrowser
from tkinter import *
import WebpageGUI
import WebpageGUIFileTrans

"""
def createFile(self):
    f = open("GenIndex.html","w")
    f.write("Stay tuned for our amazing summer sale!")
    #open and read the file after the appending:
    f = open("GenIndex.html","r")
    print(f.read())
    f.close()
    """
#Command called in WebpageGUIFileTrans to allow user to browse files and select one
def browse(self):
    filename = filedialog.askdirectory()
    print(filename)
    return(filename)

    
    #Command called in GUI to write the custome text along with opening the HTML file. 
def newBody(self):
    f = open("GenIndex.html","w")
    body =""" <html><body>{}</body></html> """.format(self.txtBody.get())
    f.write(body)
    f = open("GenIndex.html","r")
    print(f.read())
    f.close()
    #For mac users: url = "File:/Users/jeffwiley/Documents/GitHub/Python-Unit/Python_Unit/Web Page Generator/GenIndex.html"
    url = "GenIndex.html" #For PC Users
    webbrowser.open_new_tab(url)
    
