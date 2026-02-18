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


# accounts
class Account():
    def __init__(self, balance, acc_no):
        self.bal = balance
        self.account_no = acc_no

    def debit(self, amount):
        self.bal -= amount
        print("Rs. ", amount, "debited from your bank account.")
        print("Total balance in you bank account is: ", self.bal)

    def credit(self, amount):
        self.bal += amount
        print("Rs. ", amount, "debited from your bank account.")
        print("Total balance in you bank account is: ", self.bal)
    
    def get_balance(self):
        return self.bal

account1 = Account(25000, "123456AIB")
account2 = Account(98000, "256978CRE")
account1.debit(1000)
account1.credit(1600)
print("Balance of Account1 is: ",account1.bal,  "Account_No. of Account1 is: ", account1.account_no)

        