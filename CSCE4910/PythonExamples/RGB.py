'''
A simple GUI that displays 3 bars.One for Red color; one for Green color; and 
one for Blue color. All three values are store on three different variables
that can be used for other operations such as passing to other functions.

Jorge Cardona®
'''

from tkinter import *
import tkinter as tk

#Function read the RGB bars
def sel():
   selection1 = "Red = " + str(var1.get())
   selection2 = "Green = " + str(var2.get())
   selection3 = "Blue = " + str(var3.get())
   label1.config(text = selection1)
   label2.config(text = selection2)
   label3.config(text = selection3)
   R = var1.get()
   G = var2.get()
   B = var3.get()
   print("RED: %d, GREEN: %d, BLUE: %d" %(R, G, B))
   
#Our main object
mainWindow = Tk()
mainWindow.title("RGB SELECTION")

#Variable Declariations
var1 = tk.IntVar()
var2 = tk.IntVar() 
var3 = tk.IntVar()


#========================== Scroll Bars aka scales =============================
container1 = Frame(mainWindow)
container1.pack()

#scale1 = Scale( container1, variable = var1, fg="red", bg="red" )
scale1 = Scale( container1, variable = var1, bg="white", 
                troughcolor="red", activebackground="red", 
                highlightcolor="red", length = 200, width = 30, from_ = 0, to = 255 )

scale1.pack(side = LEFT)


scale2 = Scale( container1, variable = var2,bg="white",
                troughcolor="green", activebackground="green",
                highlightcolor="green", length = 200, width = 30, from_ = 0, to = 255)

scale2.pack(side = LEFT)


scale3 = Scale( container1, variable = var3, bg="white", 
                troughcolor = "blue", activebackground="blue", 
                highlightcolor="blue", length = 200, width = 30, from_ = 0, to = 255 )

scale3.pack(side = LEFT)


#=============================== Button To Show Our Selections ===========================
container2 = Frame(mainWindow)
container2.pack()

button1 = Button(container2, text="Set Value", bg="red", fg="red", command=sel)



#=============================== Loading All Componnents  =================================
container3 = Frame(mainWindow)
container3.pack()

label1 = Label(container3)
label1.pack(side = LEFT)

label2 = Label(container3)
label2.pack(side = LEFT)

label3 = Label(container3)
label3.pack(side = LEFT)

button1.pack()

mainWindow.mainloop()
