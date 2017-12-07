import numpy
from array import*
import pickle
import array
from ola.ClientWrapper import ClientWrapper     
from socket import *


#OLA Variables and Objects
RGB = '0'
data = array.array('B')
wrapper = ClientWrapper()
client = wrapper.Client()
universe = 1


# Set the socket parameters
#HOST = '192.168.1.101'
HOST = "localhost"
PORT = 6456
buf = 4096
address = (HOST, PORT)

# Create socket
UDPSock = socket(AF_INET,SOCK_DGRAM)

def DmxSent(state):
    if not state:
        wrapper.Stop()
        
    print("DmxSent(state):")
    


def JorgeDMX():      


    global client
    global universe
    global data
    global wrapper
    global address
    
    # Send messages
    msg = "Give me RGB"
    

    while True:
        print ("About To Send TO Server")
        if(UDPSock.sendto(msg.encode(), address)):
            data, address = UDPSock.recvfrom(buf)
            clientData = pickle.loads(data)
            if not data:
                print ("No data from server")
                break
            else:
                #temp = array.array('B')
                #temp.extend(clientData)
                #print temp
                
                data.extend(clientData)
                print clientData
                client.SendDmx(universe, data, DmxSent)                                        
            
            wrapper.Run()
        else:
            print("DID NOT SEND!")

            
    #Close socket                                                                          
    UDPSock.close()    
    
    
if __name__ == '__main__':
    JorgeDMX()
