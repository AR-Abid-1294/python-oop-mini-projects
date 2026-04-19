from employees_manager import *

class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager()

    def printMenu(self):
        messages = ["1. Add a new employee",
                    "2. List all employees",
                    "3. Delete employees bye age range",
                    "4. Update employee salaries by name",
                    "5. Close the program"]
        print("\n" + "\n".join(messages))
        command = input(f"Enter your command (1 to {len(messages)}): ")
        return command
    
    def run(self):
        while True:
            cmnd = self.printMenu()

            if cmnd == "1":
                print("Enter employee data")
                name = input("Name of the new employee: ")
                age = int(input("Age of the new employee: "))
                salary = input("Salary of the new employee: ")
                self.manager.addEmployee(name, age, salary)

            elif cmnd == "2":
                self.manager.listEmployees()

            elif cmnd == "3":
                starting_age = int(input("Enter age from: "))
                ending_age = int(input("Enter age to: "))
                self.manager.deleteEmployees(starting_age, ending_age)

            elif cmnd == "4":
                employee_name = input("Enter the employee name: ")
                new_salary = input("Enter new salary: ")
                self.manager.updateSalary(employee_name, new_salary)

            elif cmnd == "5":
                print("Closing the program..")
                break
                
            else:
                print("Invalid Command")
