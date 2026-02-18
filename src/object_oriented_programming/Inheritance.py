# Inheritance 1 single-level
'''class Person:
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
'''
# Inheritance 2 multi-level
#LibrarymanagementsystemusingOOPs
class LibraryItem():
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display_info(self):
        print("Title of book is: ", self.title)
        print("Author: ", self.author)

class Books(LibraryItem):
    def __init__(self, title, author, pages):
        super().__init__(title, author) 
        self.pages = pages
    def display_info(self):
        super().display_info()
        print("The no. of pages are: ", self.pages)
        print("Type: BOOK")

class Magazine(LibraryItem):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.issue_number = issue_number
    def display_info(self):
        super().display_info()
        print("The issue number is: ", self.issue_number)
        print("Type: MAGAZINE")

class DVD(LibraryItem):
    def __init__(self, title, author, duration):
        super().__init__(title, author)
        self.duration = duration
    def display_info(self):
        super().display_info()
        print("Duration of the DVD is: ", self.duration, "minutes")
        print("Type: DVD")

book1 = Books("It starts with us", "Colleen Hoover", 400)
magazine1 = Magazine("Vogue", "Editor team", 101 )
dvd1 = DVD("Iot Basics", "Quadratech_team", 55 ) 
       
book1.display_info()
magazine1.display_info()
dvd1.display_info()