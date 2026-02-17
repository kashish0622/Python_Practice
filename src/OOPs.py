class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        total = sum(self.marks)
        print("Hello,", self.name, "Your average score is: ", total/5 )

        

s1 = Student("Kashish", [98, 95, 99, 92, 91])
s1.average()  

