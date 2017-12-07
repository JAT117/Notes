'''
This Script will only sent a single frame
It is found at: https://www.openlighting.org/ola/developer-documentation/python-api/
'''

import array
from ola.ClientWrapper import ClientWrapper

def DmxSent(state):
    wrapper.Stop()

universe = 1
data = arra.array('B', [10, 50, 255])
wrapper = ClientWrapper()
client = wrapper.Client()
client.SendDmx(universe, data, DmxSent)
wrapper.Run()
