from socket import *
import numpy
#from array import*
import pickle
from Tkinter import *
from tkColorChooser import askcolor
import array


#OLA Variables Preps
RGB = '0'
rgbToClients = array.array('B')


#Globals
flag1 = 0

# Set the socket parameters
HOST = '192.168.1.100'
#HOST = "localhost"
PORT = 6454
buf = 4096
address = (HOST, PORT)


# Create socket
UDPSock = socket(AF_INET, SOCK_DGRAM)
#Connect to the given PORT AND HOST
UDPSock.bind(address)


def RGBColors():
    global RGB
    global rgbToCLients
    #---------------> Returns a tuple, ((R, G, B), HexColor)
    (RGB, HEXColor) = askcolor(color="#6A9662", title = "SELECT A COLOR")
    
    
    global flag1 
    '''
    if (flag1 == 1):
      #Remove From Window for New Inputs
    rgbToClients.remove(RGB[0])
    rgbToClients.remove(RGB[1])
    rgbToClients.remove(RGB[2])
    flag1 = 0
    
    '''
    
    #global data
    rgbToClients.append(RGB[0])
    rgbToClients.append(RGB[1])
    rgbToClients.append(RGB[2])
    flag1 = 1
    
    
    
    print ("Will send: ")
    print rgbToClients
    
    
def JorgeDMX():
    
    #OLA Implementation
    global rgbToClients


    while True:
        global rgbToCliets
        print("About to get")
        data,addr = UDPSock.recvfrom(buf)
        print("I got: ")
        print data
        print("\n")
        
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

            #print("Should not See this")
            UDPSock.sendto( pickle.dumps(rgbToClients), addr)
            #temp = array.array('B')
            #temp.extend(sendToClient)
            # print temp
            global flag1 
            if (flag1 == 1):
                #Remove From Window for New Inputs
                rgbToClients.remove(RGB[0])
                rgbToClients.remove(RGB[1])
                rgbToClients.remove(RGB[2])
                flag1 = 0
                

if __name__ == '__main__':
    JorgeDMX()
    
    # Close socket
    UDPSock.close()
