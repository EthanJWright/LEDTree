import time, threading

def print_stuff():
    print(time.ctime())

def foo():
    threading.Timer(10, print_stuff).start()
    while(True):
        time.sleep(1)
        print 'test'


foo()
