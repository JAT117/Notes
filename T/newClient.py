import numpy
from array import*
import pickle
import array
from ola.ClientWrapper import ClientWrapper     
from socket import *


#OLA Variables and Objects
RGB = '0'
dataFromServer = array.array('B', [255])
wrapper = ClientWrapper()
client = wrapper.Client()
universe = 1


# Set the socket parameters
HOST = '192.168.1.102'
#HOST = "localhost"
PORT = 6454
buf = 4096
address = (HOST, PORT)

# Create socket and Connet to the given PORT and HOST
UDPSock = socket(AF_INET,SOCK_DGRAM)
#UDPSock.bind(address)

def DmxSent(state):
    if not state:
        wrapper.Stop()
        
   
def JorgeDMX():      

    global client
    global universe
    global dataFromServer
    global wrapper
    global address
    
    # Send messages
    msg = b'Hello World!'
    

    while True:
        #print ("About To Send TO Server")
        UDPSock.sendto(msg, address)
        print("MESSAGE SENT")
        rgbValues, address = UDPSock.recvfrom(buf)
        print("Received, wrapped, : ")
        print rgbValues
        rgbToDMX = pickle.loads(rgbValues)
        print("Unwrapped format: ")
        print rgbToDMX
        if not rgbValues:
            print ("No data from server")
            break
        else:
            #temp = array.array('B')
            #temp.extend(clientData)
            #print temp
            
            dataFromServer.extend(rgbToDMX)
            #print dataFromServer[1]
            if (dataFromServer[1] == 0):
                dataFromServer[1] = 1
            for i in range(0,100):
                client.SendDmx(universe, dataFromServer, DmxSent)                                        
                wrapper.Run()
            wrapper.Run()
    else:
        print("DID NOT SEND!")
            
            
    #Close socket                                                                          
    UDPSock.close()    
    
    
if __name__ == '__main__':
    JorgeDMX()
