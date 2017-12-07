'''
This script sends multimple frames 
This example was found at:
https://www.openlighting.org/ola/developer-documentation/python-api/

'''
import array
from ola.ClientWrapper import CLientWrapper

wrapper = None
i = 0
TICK_INTERVAL = 100 #100 ms

def DmxSent(state):
    if not state.Succeeded():
        wrapper.Stop()


def SendFMXFrame():
    #Schedule a function call in 100ms
    #We do this first in case the frame computation takes a long time.
    wrapper.AddEvent(TICK_INTERVAL, SendDMXFrame)


    #Here is where we compute our frames
    data = array.array('B')
    global i
    data.append(i % 255)
    i += 1


    #Now send that frame
    wrapper.Client().SendDmx(1, data, DmxSent)


wrapper = ClientWrapper()
wrapper.AddEvent(TICK_INTERVAL, SendDMXFrame)
wrappper.Run()
