#A client that uses AF_INET family connections
import socket
 
HOST = ''              #The remote host. All available or any.
PORT = 50007           #The same port as used on Server

cSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cSocket.connect((HOST, PORT))



temp = 0
while (temp != 10):
    #SENDS DATA IN BYTES
    cSocket.sendall('Hello, World!'.encode())
    #cSocket.sendto('Hello, World!'.encode(), (HOST, PORT))
    
    #RECEIVES DATA IN BYTES
    data = cSocket.recv(1024)
    
    #cSocket.close()
    
    print ('Server said: ', repr(data.decode()), temp)
    
    temp = temp + 1
    
cSocket.close()
