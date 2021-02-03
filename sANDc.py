import sys
import socket

clientS = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dataSize = 2048

HOST = '192.168.1.101'
PORT = 6454
address = (HOST, PORT)


if sys.argv[1:] == ['server']:
    clientS.bind(address)
    print("Listening at %s" %clientS.getsockname())

    while True:
        data, address = clienS.recvfrom(dataSize)
        print("The client is at %s and said: %s" %(address, data.decode()))
        clientS.sendto("The data you sent me was %d bytes long from %s".encode() %(len(data), address))

elif sys.argv[1:] == ['client']:
    clientS.sendto("Hi server!".encode(), address)
    data, address = clientS.recvfrom(dataSize)
    print("The server is  at %s and said: %s" %(address, data.decode()))

    temp = 10
    while (temp != 0):
        clientS.sendto("Hi Server: ".encode(), address)
        temp = temp -1

    
else:
    print("Usage: sANDc.py  client|server")
