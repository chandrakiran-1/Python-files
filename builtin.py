import threading
import time

# Define your own thread class
class MyThread(threading.Thread):
    def run(c):  # run() method will execute when thread starts
        for i in range(3):
            print("Custom Thread ->", i)
            time.sleep(2)

# Create object of MyThread (like normal class)
t1 = MyThread()
t1.start()   # this calls run() in background
t1.join()    # wait till it finishes

print("Main program finished")
