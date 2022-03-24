from threading import *
class Test:
    def display(self):
        for i in range(10):
            print('childthread-2')
obj=Test()
t=Thread(target=obj.display)
t.start()
for i in range(10):
    print('mainthread-2')