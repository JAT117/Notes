from gpiozero import LED #sudo apt-get install python3-gpiozero
from time import sleep

myLED = LED(18) #myLED is connected on pin #18

temp = 0
while(temp != 10):
   # myLED.on()
 
    myLED.toggle()
    
    sleep(0.5)
    temp += 1

myLED.off()
  
