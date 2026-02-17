class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        total = sum(self.marks)
        print("Hello,", self.name, "Your average score is: ", total/5 )

        

s1 = Student("Kashish", [98, 95, 99, 92, 91])
s1.average()  
s2 = Student("Diya", [99, 97, 93, 95, 91])
s2.average()  
s3 = Student("Anshu", [88, 96, 100, 88, 87])
s3.average()  
s4 = Student("Rishabh", [97, 90, 89, 82, 71])
s4.average()  
s5 = Student("Zeven", [58, 63, 42, 55, 99])
s5.average()  

