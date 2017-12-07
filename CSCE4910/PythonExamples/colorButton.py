"""#!/usr/local/bin/python3"""
#!/usr/bin/env python3

#import module as alias
from tkinter import *
import tkinter as tk
from tkinter import ttk

#Create class instance to variable
win = tk.Tk()   

# Add a title to outter window      
win.title("Python GUI")

myLabel = ttk.Label(win, text = "My Lable")
myLabel.grid(column=0, row=0)

#Event Button handler
def clickMe():
    #Modifies myButton
    myButton.configure(text = "***I Have Been Clicked***") 
    
    #Modifies myLabel
    myLabel.configure(foreground = 'red')
    myLabel.configure(text = 'Now I am Red')

myButton = ttk.Button(win, text = "Click Me!", command = clickMe)
myButton.grid(column = 1, row = 0)




win.mainloop()
