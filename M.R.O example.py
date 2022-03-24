class a:
    def myname(self):
        print('from class a')
class b(a):
    def myname(self):
        print('from class b')
class c(a):
    def myname(self):
        print('from class c')
class d(b,c):
    def myname(self):
        pass
print(d.__mro__)
print(c.mro())