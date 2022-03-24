def prime(n):
    for i in range(2,(n/2)+1):
        if(n%i == 0):
            return False
            break
        else:
            return True
a= int(input('enter the number:'))
if prime(a) == True:
    print(a, 'is a prime number')
else:
    print('not a prime')
            
        