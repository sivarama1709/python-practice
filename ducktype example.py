class Duck:
    def talk(self):
        print('duck...duck...')
class Cat:
    def talk(self):
        print('meow...meow...')
class Human:
    def talk(self):
        print('blah...blah...')
def f1(obj):
    obj.talk()
l=[Duck(), Cat(), Human()]
for obj in l:
    f1(obj)