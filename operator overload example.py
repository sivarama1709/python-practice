class Book:
    def __init__(self,pages):
        self.pages = pages
    def __add__(self,other):
        return self.pages + other.pages
b1=Book(250)
b2=Book(300)
print('total no of pages are:',b1+b2)