class GP:
    def m1(self):
        print('parent class')
class P(GP):
    def m2(self):
        print('intermediate class')
class C(P):
    def m3(self):
        print('child class ')
t=C()
t.m1()
t.m2()
t.m3()