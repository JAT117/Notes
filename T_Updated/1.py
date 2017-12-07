from socket import *
import numpy
from array import*
import pickle
from Tkinter import *
from tkColorChooser import askcolor
import array


#OLA Variables Preps
RGB = '0'
data = array.array('B')


#Globals
flag1 = 0

# Set the socket parameters
#HOST = '192.168.1.101'
HOST = "localhost"
PORT = 6454
buf = 4096
address = (HOST, PORT)


# Create socket
UDPSock = socket(AF_INET,SOCK_DGRAM)

'''
def RGBColors():
    global RGB
    #---------------> Returns a tuple, ((R, G, B), HexColor)
    (RGB, HEXColor) = askcolor(color="#6A9662", title = "SELECT A COLOR")
    
    global flag1 
    if (flag1 == 1):
        #Remove From Window for New Inputs
        data.remove(RGB[0])
        data.remove(RGB[1])
        data.remove(RGB[2])          
        flag1 = 0
        
    
    global data
    data.append(RGB[0])
    data.append(RGB[1])
    data.append(RGB[2])
    flag1 = 1
    
    print data
    
'''    
def JorgeDMX():
    
    #OLA Implementation
    global data


    while True:
        global data
        print("About to get")
        data,addr = UDPSock.recvfrom(buf)
        #sendToClient = pickle.loads(data)
        if not data:
            print ("Client has exited!")
            break
        else:

            #Color Wheel Implementation
            root = Tk()
            Button(root, text = 'Choose A  Color', command = RGBColors).pack(side = LEFT, padx = 10)
            Button(text = 'Set Color', command = root.quit()).pack(side = LEFT, padx=10, pady=10)
            root.mainloop()
            
            UDPSock.sendto( pickle.dumps(data), addr)
            #temp = array.array('B')
            #temp.extend(sendToClient)
            # print temp


            
            
       


if __name__ == '__main__':
    JorgeDMX()
    
    # Close socket
    UDPSock.close()
