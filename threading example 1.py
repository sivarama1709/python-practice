import threading
class X(threading.Thread):
    def run(self):
        for p in range(1,20):
            print(p)
class Y(threading.Thread):
    def run(self):
        for q in range(21,30):
            print(q)
x1=X()
y1=Y()
x1.start()
y1.start()