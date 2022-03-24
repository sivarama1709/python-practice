n=int(input('enter no of students:'))
for i in range(n):
    Name=input('enter name of the student:')
    Marks=int(input('enter the marks:'))
    class student:
        def __init__(self,Name,Marks):
            self.Name=Name
            self.Marks=Marks
        def display(self):
            print('hi,',self.Name)
            print('marks',self.Marks)
        def grade(self,Marks):
            if self.Marks>=60:
                print('first class')
            elif self.Marks>=50:
                print('second class')
            elif self.Marks>=40:
                print('third class')
            else:
                print('failed')
s1=student(Name,Marks)
s1.display()
s1.grade(Marks)
s2=student(Name,Marks)
s2.display()
s2.grade(Marks)