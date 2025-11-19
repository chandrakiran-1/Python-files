import threading
import time

def display():
    for i in range(5):
        print("This is display thread")
        time.sleep(1)

def show():
    for i in range(5):
        print("This is show thread")
        time.sleep(1)

t1 = threading.Thread(target=display)
t2 = threading.Thread(target=show)

t1.start()
t2.start()

t1.join()
t2.join()

print("Both threads completed")
