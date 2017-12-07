'''
This cript received framves
This examnple was found at:
https://www.openlighting.org/ola/developer-documentation/python-api/

'''

from ola.ClientWrapper import ClientWrapper

def NewData(data):
    print data


universe = 1

wrapper = ClientWrapper()
client = wrapper.Client()
client.RegisterUniiverse(universe, client.REGISTER, NewData)
wrapper.Run()
