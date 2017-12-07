#! /usr/bin/env python

'''
The line above indicates to use python
it will be the same, perhaps better, if we used:
#!/usr/local/bin/python
          Or:
#!/Path/To/Python/Interpretator

----Stick to the first one----

Once the file is completed:
chmod +x file.py

Now you dont have to use 'python file.py' everytime you want to use the script 

usage:
./file.py
'''

def main():
    for i in range(1, 10):
        print("I am an executable file")

if __name__ == '__main__':
    #print("I was just now updated since I became an executable script.\n")
    main()
