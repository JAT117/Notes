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

         #Place that lable IN "win"
ttk.Label(win, text = "My Lable").grid(column=0, row=1)

#======================
# Start GUI
#======================
win.mainloop()
