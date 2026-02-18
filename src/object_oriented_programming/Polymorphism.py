# Method override
#EmployeeSalarySystem
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