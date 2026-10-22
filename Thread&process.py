
import threading
from time import time


def show():
    print("This is a child thread")

t=threading.Thread(target=show)
t.start()
print("This is a main thread")

class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print("\n This is a child thread")
t1=MyThread()
t1.start()
print("\n This is a main thread !!!")
print("\n*******************")
class Demo:
    def num(self):
        for i in range(1,6):
            print("\n The number is ",i)
    def double(self):
        for i in range(1,6):
            print("\n The double of ",i," is ",2*i)
    def squre(self):
        for i in range(1,6):
            print("\n The square of ",i," is ",i*i)


obj=Demo()
t1=threading.Thread(target=obj.num)
t2=threading.Thread(target=obj.double)
t3=threading.Thread(target=obj.squre)

t1.start()
 
t2.start()  
t3.start()

t1.join()
t2.join()
t3.join()

print("\n This is a main thread !!!")