#!/usr/bin/env python3                                                                                

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

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

#Global Array/List tkinter
colors = ["Blue", "Gold", "Red"]

#Action Handler
def radCall():
    #Gets the selected value aka clicked option
    radSel=radVar.get()
    
    if   radSel == 0: 
        win.configure(background=colors[0])
        
    elif radSel == 1: 
        win.configure(background=colors[1])
        
    elif radSel == 2: 
        win.configure(background=colors[2])
        

#tkinter variable to hold I/O selection
radVar = tk.IntVar()


#Set Var outside range to avoid accidental selections
radVar.set(99)    

for i in range(3):
    #curRad = 'rad' + str(i)  
    #----------------------(window,   color,     Button_clicked,  Button_#,  Action_Handler)
    curRad = tk.Radiobutton(win, text=colors[i], variable=radVar, value=i,   command=radCall)
    curRad.grid(column=i, row=6, sticky=tk.W)
    
#--------------------------------------END OF RADIO BUTTONS-------------------------------------------




#------------------------------------------SCROLLED TEXT------------------------------------------------
scrolW  = 20 #Box field Hight
scrolH  =  2 #Box field length

#.....................................(window,   width,         hight,     \n at words)
scrollField = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD)
scrollField.grid(column=0, sticky='WE', columnspan=3) #Columnspan = how much it will cover
#--------------------------------------END OF SCROLLED TEXT--––-----------------------------------------


#Adding a Button
myButton = ttk.Button(win, text="Click Me!", command=clickMe)   
myButton.grid(column=2, row=1) #Possition
#myButton.configure(state = "disable")
#myButton.configure(state = "disabled")
 



win.mainloop()
