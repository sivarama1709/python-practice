class Test:
    count=0
    def __init__(self):
        Test.count=Test.count+1
    @classmethod
    def num_object(cls):
        print('no of objects created',cls.count)
t1=Test()
t2=Test()
Test.num_object()
t3=Test()
t4=Test()
t5=Test()
Test.num_object()