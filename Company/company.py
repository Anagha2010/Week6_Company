class Company:
    # class constructor
    def __init__(self, name):
        # attribute for name of company
        self.name = name
        # attribute for list of employees
        self.employees = []

    # methods

    # adds employee to the employees list
    def hire_employee(self, employee):
        # appends employee to the list
        self.employees.append(employee)
        print(f"\n{employee.name} has been hired at {self.name}.")

    # Lists all employees
    def list_employees(self):
        print(f"\n~~~~~Employees at {self.name}:~~~~~")
        for employee in self.employees:
            print(f"{employee.name} - {employee.role}\n{'~' * 20}")

    # removes employee from the list
    def fire_employee(self, employee):
        if employee.role != "Owner":
            # removes employee from the list unless employee is also the owner
            self.employees.pop(self.employees.index(employee))

        else:
            print(f"\nCannot fire {employee.name}, {employee.pronoun} owns the firm!")