# Inheritance 
class Person:
    def __init__(self, name, age):
        self.name= name
        self.age= age
    def display_person(self):
        print("Name: ", self.name)
        print("Age: ", self.age)

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age) 
        self.student_id = student_id

    def display_student(self):
        print("Student ID: ", self.student_id)  

s1 = Student("Anuj Kumar", 16, "STUD101")

s1.display_person()
s1.display_student()

