#!/usr/bin/env python3                                                                                

import tkinter as tk
from tkinter import ttk

# Create instance
win = tk.Tk()   

# Add a title       
win.title("Python GUI")



#Handles Button Clicked 
def clickMe():
    #When clicked, change name of button.
    myButton.configure(text='Hello ' + name.get()+ ' ' + number.get() + ' Enable: ' + chVarEn.get() +' Disable: ' + chVarUn.get())



#Lable INSIDE our win (Window)
ttk.Label(win, text="Enter a name:").grid(column=0, row=0)



#String Variable
name = tk.StringVar()



#BOX for INPUT inside win of width 12 and value stored on  Var name
inputBox = ttk.Entry(win, width = 12, textvariable = name)
inputBox.grid(column = 0, row = 1) #Possition
inputBox.focus()



#Adds another lable to our win and possitions it
ttk.Label(win, text="Choose a number:").grid(column=1, row=0)



#tkinter var declaration
number = tk.StringVar() 



#Drop down BOX inside win size we and value stored on Var 'number'
dropDownNumber = ttk.Combobox(win, width = 12, textvariable = number, state = 'readonly')
dropDownNumber['values'] = (1, 2, 4, 42, 100) #Tuple of Ints
dropDownNumber.grid(column=1, row=1) #Possition
dropDownNumber.current(0) #Default Value




# Creating three checkbuttons
chVarDis = tk.IntVar()                                             #Gray out BUTTON  
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disabled')
check1.select() #Shows a selected button
check1.grid(column=0, row=4, sticky=tk.W)                   



chVarUn = tk.IntVar()
chVarUn = tk.StringVar()
check2 = tk.Checkbutton(win, text="UnChecked", variable=chVarUn) #variables is where inputs are stored
check2.deselect() #Shows a unselected BUTTON
check2.grid(column=1, row=4, sticky=tk.W)                   




#chVarEn = tk.IntVar()
chVarEn = tk.StringVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn) #chVarEn will hold the selection I/O
check3.select() #Shows a selected BUTTON
check3.grid(column=2, row=4, sticky=tk.W)   




#Adding a Button
myButton = ttk.Button(win, text="Click Me!", command=clickMe)   
myButton.grid(column=2, row=1) #Possition
#myButton.configure(state = "disable")
#myButton.configure(state = "disabled")
 





win.mainloop()
