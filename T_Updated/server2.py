import pickle
from socket import *
import array
# Set the socket parameters
host = "localhost"
port = 21567
buf = 4096
addr = (host,port)

# Create socket and bind to address
UDPSock = socket(AF_INET,SOCK_DGRAM)
UDPSock.bind(addr)

# Receive messages
while 1:
    data,addr = UDPSock.recvfrom(buf)
    clientData = pickle.loads(data)
    if not data:
        print ("Client has exited!")
        break
    else:
        temp = array.array('B')
        temp.extend(clientData)
        print temp
        

# Close socket
UDPSock.close()
