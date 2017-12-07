'''
Ok I will call another script from this file.
This other script is called 2.py
it has two def function and a main function.
lets see the difference when using 
if __name__='__main__':
main()
vs not using it and havinf functions in it.
'''
from two import temp

for i in range(0,10):
    print(i)

print("calling temp()")
temp()
