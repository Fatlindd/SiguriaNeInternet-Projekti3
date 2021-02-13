# __________________________
#| Punuan:                 |
#| Fatlind Thaçi           |
#| Florent Kafexholli      |
#| Enis Hoti               |
#|                         |
#| Python Application For  |
#|     COPY&MOVE Files     |
#|_________________________|

import shutil 
import tkinter as tk 
from tkinter import *
from tkinter import messagebox, filedialog 
     
def TkinterWidgets(): 
    link_Label = Label(root, text ="File për kopjim : ", fg="#092635",bg = "#CEE1CE" ,font='Courier 20 bold') 
    link_Label.grid(row = 1, column = 0, pady = 3, padx = 5) 

    root.sourceText = Entry(root, width = 50, textvariable = sourceLocation) 
    root.sourceText.grid(row = 1, column = 1, ipady = 5, ipadx = 5, columnspan = 2) 
   

    source_browseButton = Button(root, text ="Browse", command = SourceBrowse,background='orange', width = 15, borderwidth=1, font="sans 10 bold") 
    source_browseButton.grid(row = 1, column = 3, ipady = 2, padx = 5) 
     
    destinationLabel = Label(root, text ="Destinacioni File : ", fg ="#092635" , bg="#CEE1CE", font='Courier 20 bold') 
    destinationLabel.grid(row = 2, column = 0, ipady = 5, ipadx = 5) 
     
    root.destinationText = Entry(root, width = 50, textvariable = destinationLocation) 
    root.destinationText.grid(row = 2, column = 1, ipady = 5, ipadx = 5, columnspan = 2) 
     
    dest_browseButton = Button(root, text ="Browse", command = DestinationBrowse, background='orange', width = 15, borderwidth=1, font="sans 10 bold") 
    dest_browseButton.grid(row = 2, column = 3,  ipady = 2, padx = 5) 
     
    copyButton = Button(root, text ="Copy File", command = CopyFile,background='orange', width = 15, borderwidth=1, font="sans 10 bold") 
    copyButton.grid(row = 3, column = 1, ipady = 2, padx = 5) 
     
    moveButton = Button(root, text ="Move File", command = MoveFile,background='orange', width = 15, borderwidth=1, font="sans 10 bold") 
    moveButton.grid(row = 3, column = 2, ipady = 2, padx = 5) 
 
def SourceBrowse(): 
     
    root.files_list = list(filedialog.askopenfilenames(initialdir ="Users/ KobitPC / Desktop / Projekti3_SiguriaNeInternet")) 
     
    root.sourceText.insert('1', root.files_list) 
     
def DestinationBrowse(): 

    destinationdirectory = filedialog.askdirectory(initialdir ="Users/ KobitPC / Desktop / Projekti3_SiguriaNeInternet") 
 
    root.destinationText.insert('1', destinationdirectory) 
     
def CopyFile(): 

    files_list = root.files_list 
 
    destination_location = destinationLocation.get() 
 
    for f in files_list: 

        shutil.copy(f, destination_location) 
 
    messagebox.showinfo("INFO","FILE ËSHTË KOPJUAR ME SUKSES!") 
     
def MoveFile(): 

    files_list = root.files_list 

    destination_location = destinationLocation.get() 

    for f in files_list: 
         
        shutil.move(f, destination_location) 
 
    messagebox.showinfo("INFO","FILE U TRANSFERUA ME SUKSESE!") 
 
root = tk.Tk() 
#root.option_add('*Font', 10)
root.geometry("800x150") 

root.title("Copy&Move") 
root.config(background = "#CEE1CE") 

# Creating tkinter variable 
sourceLocation = StringVar() 
destinationLocation = StringVar() 

# Calling the CreateWidgets() function 
TkinterWidgets() 

# Defining infinite loop 
root.mainloop() 
