class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    
    def give_raise(self, amount):
        self.salary += amount
    
    def display_employee(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: Php.{self.salary}")


employee1 = Employee("Jane Doe", "Computer Scientist", 150000)

employee1.give_raise(200000)

employee1.display_employee()
