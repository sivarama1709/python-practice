class student:
    def setName(self,name):
        self.Name=name
    def getName(self):
        return self.Name
    def setMarks(self,marks):
        self.Marks=marks
    def getMarks(self):
        return self.Marks
n=int(input('enter the no of students:'))
for i in range(n):
    s=student()
    Name=input('enter name')
    s.setName(Name)
    Marks =int(input('enter marks:'))
    s.setMarks(Marks)
    print('name:',s.getName)
    print('marks:',s.getMarks)
    print()