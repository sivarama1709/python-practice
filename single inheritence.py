class Parent:
    def m1(self):
        print('parent class')
class Child(Parent):
    def m2(self):
        print('child class')
c=Child()
c.m1()
c.m2()