#!/usr/bin/env python3                                                                                

import tkinter as tk
from tkinter import ttk

# Create instance
win = tk.Tk()   

# Add a title       
win.title("Python GUI")


#-------------------------------------------INPUT FIELD-------------------------------------------
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
#------------------------------------END OF INPUT FIELD-------------------------------------------





#--------------------------------------DROP DOWN NUMBERS------------------------------------------
#Adds another lable to our win and possitions it
ttk.Label(win, text="Choose a number:").grid(column=1, row=0)

#tkinter var declaration
number = tk.StringVar() 

#Drop down BOX inside win size we and value stored on Var 'number'
dropDownNumber = ttk.Combobox(win, width = 12, textvariable = number, state = 'readonly')
dropDownNumber['values'] = (1, 2, 4, 42, 100) #Tuple of Ints
dropDownNumber.grid(column=1, row=1) #Possition
dropDownNumber.current(0) #Default Value
#--------------------------------------END OF DROP DOWN NUMBERS------------------------------------





#-------------------------------------------CHECK BUTTONS-------------------------------------------
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
#--------------------------------------END OF CHECK BUTTONS-------------------------------------------





#-------------------------------------------RADIO BUTTONS---------------------------------------------
#Global Variables tkinter
COLOR1 = "Blue"
COLOR2 = "Gold"
COLOR3 = "Red"

#Action Handler
def radCall():
    #Gets the selected value aka clicked option
    radSel = radVar.get()
    
    if radSel == 1:   
        win.configure(background=COLOR1)
        
    elif radSel == 2: 
        win.configure(background=COLOR2)
        
    elif radSel == 3: 
        win.configure(background=COLOR3)
        
#tkinter variable to hold I/O selection
radVar = tk.IntVar()

#-----------------  -(window,   color,  Button_clicked,  Button_#,  Action_Handler)
rad1 = tk.Radiobutton(win, text=COLOR1, variable=radVar, value=1, command=radCall)
rad1.grid(column=0, row=5, sticky=tk.W, columnspan=3)   

rad2 = tk.Radiobutton(win, text=COLOR2, variable=radVar, value=2, command=radCall)
rad2.grid(column=1, row=5, sticky=tk.W, columnspan=3)  

rad3 = tk.Radiobutton(win, text=COLOR3, variable=radVar, value=3, command=radCall)
rad3.grid(column=2, row=5, sticky=tk.W, columnspan=3)

#--------------------------------------END OF RADIO BUTTONS-------------------------------------------






#Adding a Button
myButton = ttk.Button(win, text="Click Me!", command=clickMe)   
myButton.grid(column=2, row=1) #Possition
#myButton.configure(state = "disable")
#myButton.configure(state = "disabled")
 





win.mainloop()
