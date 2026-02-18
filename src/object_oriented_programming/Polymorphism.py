# Method override
#EmployeeSalarySystem
'''
class Employee:
    def calculate_salary(self):
        print("Salary calculation depends on the employee type")

class FullTimeEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary
    def calculate_salary(self):
        print("Full Time Employee salary: ", self.monthly_salary)

class PartTimeEmployee(Employee):
    def __init__(self, workinghours, hourlyrate):
        self.workinghours = workinghours
        self.hourlyrate = hourlyrate

    def calculate_salary(self):
        salary = self.workinghours * self.hourlyrate
        print("Part Time Employee Salary: ", salary)

Employees = [

    FullTimeEmployee(75000),
    PartTimeEmployee(25, 250)
]

for emp in Employees:
    emp.calculate_salary()
    '''
# method overload
class Bonus:
    def calculate_bonus(self, salary, rating = None):
        self.salary=salary
        self.rating=rating

        if rating is None:
            bonus=salary * 0.20
            print("Bonus with salary only: ", bonus)

        else:
            bonus=salary*(0.20 + rating * 0.10)
            print("Bonus with salary and rating: ", bonus)

a = Bonus()
a.calculate_bonus(500)
a.calculate_bonus(500, 5)
