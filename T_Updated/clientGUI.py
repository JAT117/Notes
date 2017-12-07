from socket import *
import numpy
from array import*
import pickle
from Tkinter import *
from tkColorChooser import askcolor
import array
#from ola.ClientWrapper import ClientWrapper                                                                           


#OLA Variables and Objects                                                                                             
RGB = '0'
data = array.array('B')
#wrapper = ClientWrapper()                                                                                             
#client = wrapper.Client()                                                                                             




# Set the socket parameters
host = "localhost"
port = 21567
buf = 4096
addr = (host,port)

# Create socket
UDPSock = socket(AF_INET,SOCK_DGRAM)



def DmxSent(state):
  #wrapper.Stop()                                                                                                      
    print("DmxSent(state):")


def RGBColors():
    global RGB
    #---------------> Returns a tuple, ((R, G, B), HexColor)                                                           
    (RGB, HEXColor) = askcolor(color="#6A9662", title = "SELECT A COLOR")

    global data
    data.append(RGB[0])
    data.append(RGB[1])
    data.append(RGB[2])

    print data

    '''                                                                                                                
    #OLA Implementation                                                                                                
    universe = 1                                                                                                       
    global client                                                                                                      
    #client.SendDmx(universe, data, DmxSent)                                                                           
    global wrapper                                                                                                     
    #wrapper.Run()                                                                                                     
    '''
    #Remove From Window for New Inputs                                                                                 
    #data.remove(RGB[0])
    #data.remove(RGB[1])
    #data.remove(RGB[2])

'''
def JorgeDMX():
    #Color Wheel Implementation                                                                                        
    root = Tk()
    Button(root, text = 'Choose A  Color', command = RGBColors).pack(side = LEFT, padx = 10)
    Button(text = 'Set Color', command = root.quit).pack(side = LEFT, padx=10, pady=10)
    root.mainloop()

    #OLA Implementation                                                                                                
    global data
    
    def_msg = "===Send Now? ===";
    print "\n",def_msg
    
    # Send messages
    while (1):
        userIn = raw_input('yes or no: ')
        if userIn!= "yes":
            break
        else:
        #if(UDPSock.sendto(a,addr)):
            if (UDPSock.sendto( pickle.dumps(data), addr)): 
                print "Sending message\n"
            universe = 1
            global client
            #client.SendDmx(universe, data, DmxSent)     
            #global wrapper
            #wrapper.Run()                                                                                                     

    # Close socket
    UDPSock.close()

'''









    
if __name__ == '__main__':
    JorgeDMX()





