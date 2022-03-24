class Parent:
    def m1(self):
        print('parent class')
class Child1(Parent):
    def m2(self):
        print('child class 1')
class Child2(Parent):
    def m2(self):
        print('child class 2')
c=Child1()
c.m1()
c.m2()
c2=Child2()
c2.m1()
c2.m2()