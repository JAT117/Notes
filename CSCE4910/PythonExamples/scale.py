from tkinter import *
import tkinter as tk

def sel():
   selection1 = "Red = " + str(var1.get())
   selection2 = "Green = " + str(var2.get())
   selection3 = "Blue = " + str(var3.get())
   label1.config(text = selection1)
   label2.config(text = selection2)
   label3.config(text = selection3)

mainWindow = Tk()
'''
var1 = DoubleVar()
var2 = DoubleVar()
var3 = DoubleVar()
'''
var1 = tk.IntVar()
var2 = tk.IntVar() 
var3 = tk.IntVar()

#======= Scroll Bars aka scales ========
container1 = Frame(mainWindow)
container1.pack()

#scale1 = Scale( container1, variable = var1, fg="red", bg="red" )
scale2 = Scale( container1, variable = var1, bg="white", 
                troughcolor="red", activebackground="red", 
                highlightcolor="red", length = 200, width = 30 )

scale2.pack(side = LEFT)

scale1 = Scale( container1, variable = var2,bg="white",
                troughcolor="green", activebackground="green",
                highlightcolor="green", length = 200, width = 30)

scale1.pack(side = LEFT)


scale3 = Scale( container1, variable = var3, bg="white", 
                troughcolor = "blue", activebackground="blue", 
                highlightcolor="blue", length = 200, width = 30 )

scale3.pack(side = LEFT)


#========= Buttons to capture the selection ===========
'''container2 = Frame(mainWindow)
container2.pack()
button1 = Button(container2, text="Set Value", bg="red", fg="red", command=sel)
button1.pack(side = LEFT)
button2 = Button(container2, text="Set Value", bg="blue", command=sel)
button2.pack(side = LEFT)
button3 = Button(container2, text="Set Value", bg="green", command=sel)
button3.pack(side = LEFT)'''
container2 = Frame(mainWindow)
container2.pack()
selR = IntVar()
selR.set(0)
selG = IntVar()
selG.set(0)
selB = IntVar()
selB.set(0)

'''
def checkR():
   if seleR.get == 0:
       labelText = Label(text="It worked").pack()
   else:
       labelText = Label(text="It DIDNT worked").pack()

def checkG():
   if seleG.get == 0:
       labelText = Label(text="It worked").pack()
   else:
       labelText = Label(text="It DIDNT worked").pack()

def checkB():
   if seleB.get == 0:
       labelText = Label(text="It worked").pack()
   else:
       labelText = Label(text="It DIDNT worked").pack()
'''
container2 = Frame(mainWindow)
container2.pack()
       
def checkRGB():
   if (selR.get == 0 and selG.get == 0 and selB.get == 0):
       labelText = Label(text="It worked").pack()
       
       #button1 = Button(container2, text="Set Value", bg="red", fg="red", command=sel)
       #button1.pack()
   else:
      code = StringVar()
      code = selR
      labelText = Label(text=code)


          
checkR =  Checkbutton(mainWindow, text="Red", variable=selR, onvalue=1, offvalue=0, height=5, width=10)
checkG =  Checkbutton(mainWindow, text="Green", variable=selG, onvalue=1, offvalue=0, height=5, width=10)
checkB =  Checkbutton(mainWindow, text="Blue", variable=selB, onvalue=1, offvalue=0, height=5, width=10)
button1 = Button(container2, text="Set Value", bg="red", fg="red", command=sel)



#============Displays the selections ==== ===========
container3 = Frame(mainWindow)
container3.pack()

#label = Label(mainWindow)
label1 = Label(container3)
label1.pack(side = LEFT)

label2 = Label(container3)
label2.pack(side = LEFT)

label3 = Label(container3)
label3.pack(side = LEFT)


checkR.pack(side = LEFT)
checkG.pack(side = LEFT)
checkB.pack(side = LEFT)
button1.pack()
mainWindow.mainloop()
