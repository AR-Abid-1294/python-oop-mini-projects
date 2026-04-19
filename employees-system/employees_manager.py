from employee import *


class EmployeesManager:
    def __init__(self):
        self.employees = list()

    def addEmployee(self, name, age, salary):
        self.employees.append(Employee(name, age, salary))

    def listEmployees(self):
        if len(self.employees) == 0:
            print("No employees available.")
        else:
            for employee in self.employees:
                print(employee)

    def deleteEmployees(self, startAge, endAge):
        for employee in self.employees[:]:
            if startAge <= employee.age <= endAge:
                print(f"Deleting employee {employee.name}")
                self.employees.remove(employee)

    def findEmployee(self, name):
        for employee in self.employees:
            if employee.name == name:
                return employee
        return None
    
    def updateSalary(self, name, new_salary):
        employee = self.findEmployee(name)
        if employee is None:
            print(f"No employee found with the name {name}.")
        else:
            employee.salary = new_salary
