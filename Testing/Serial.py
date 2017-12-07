import serial

ser = serial.Serial ("/dev/ttyAMA0")    #Open named port

ser.baudrate = 9600                     #Set baud rate to 9600

#data = ser.read(10)                     #Read ten characters from serial port to data

data = '1'
for i in range(10):
    ser.write(data)                         #Send back the received data
    print(i)
ser.close() 
