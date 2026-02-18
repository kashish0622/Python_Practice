# Employee Work System
from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def work(self):
        pass

class Developer(Employee):
    def work(self):
        print("Developer writes the code")

class Manager(Employee):
    def work(self):
        print("Manager manages the team")

developer1 = Developer()
manager1 = Manager()

developer1.work()
manager1.work()
