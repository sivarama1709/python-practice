try:
    a=int(input('enter the value of a:'))
    b=int(input('enter the value of b:'))
    c=a**b
    print('a**b=',c)
except Exception as e:
    print("can't divide by zero")
    print(e)
else:
    print('rest of the program')