class Book:
    def __init__(self,pages):
        self.pages=pages
def __add__(self,other):
    return self.pages+other.pages
b1=Book(100)
b2=Book(200)
print('total no of pages',b1+b2) 