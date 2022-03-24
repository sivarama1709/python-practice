import threading
import time
class X(threading.Thread):
    def run(self):
        for p in range (1,121):
            print(p)
            if p ==50:
                time.sleep(20)
class Y(threading.Thread):
    def run(self):
        for q in range (151,200):
            print(q)
x1=X()
y1=Y()
x1.start()
y1.start()