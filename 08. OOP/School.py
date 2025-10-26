class Student:
    def __init__(self,name, cls,id):
        self.name = name
        self.cls = cls
        self.id = id
        
    def __repr__(self):
        return f"Student: {self.name} Class: {self.cls} Id: {self.id}"
    
class Teacher:
    def __init__(self,name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self):
        return f"Teacher: {self.name} Subject: {self.subject}"

class School:
    def __init__(self,name):
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self,name, subject):
        id = len(self.teachers)+100
        teacher = Teacher(name,subject, id)
        self.teachers.append(teacher)


    def enrolled(self,name, cls, fee):
        if fee<6500:
            return f"Not Enough Money."
        else:
            id = len(self.students)+1
            stu = Student(name, cls, id)
            self.students.append(stu)
            return f"{stu} is enrolled with id: {id}. Extra Money: {fee-6500}"
        
    def __repr__(self):
        print(f"Welcome to {self.name}")
        print("-------------Our Teachers-------------")
        for techer in self.teachers:
            print(techer)

        print("-------------Our Students--------------")
        for student in self.students:
            print(student)
        return f"Thank you for the enrolled."
    

        
scl = School("Bright Star")
scl.add_teacher("Bonna Mam", "Religion")
scl.add_teacher("Ripon Sir", "Math")
scl.add_teacher("Moriam mam", "English")
scl.enrolled("Mehedi",5, 7000)
scl.enrolled("Pial",5, 5000)
scl.enrolled("Sajjad",5, 7500)
scl.enrolled("Sukonna",5,8000)
print(scl)     
