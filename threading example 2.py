import threading
class X(threading.Thread):
    def run(self):
        myfunc()
class Y(threading.Thread):
    def run(self):
        myfunc()
def myfunc():
    for p in range(1,21):
        print(p)
x1=X()
y1=Y()
x1.start()
y1.start()