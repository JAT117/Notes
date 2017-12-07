'''
This is a very simple example on fork()
The purpose is to see the syntax.
Use the time flag to see its performance
Compare it to the file thread.pyt
to get a general idea on how they both work

usage:
time python fork.py

'''
import os
import time

def main():

    #Fork 10 times
    for i in range(10):
        pid = os.fork()
        if pid:
            print 'created new process %d' % pid
            continue
        else:
            time.sleep(1)
            return

if __name__ == '__main__':
    main()
