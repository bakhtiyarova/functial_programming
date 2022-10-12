class Student:
    name=""
    course_name=""
    course=0
    def printInfo(self):
        return "Name: "+self.name+", Course: "+str(self.course)+", Course name: "
students=list()
for i in range(2):
    student=Student()
    print("________________")
    print("Enter name: ")
    student.name=input()
    print("Enter course: ")
    student.course=int(input())
    students.append(student)
for i in range(len(students)):
    for j in range(len(students)):
        if students[i].course<students[j].course:
            temp=students[i]
            students[i]=students[j]
            students[j]=temp
for student in students:
    print(student.printInfo())

