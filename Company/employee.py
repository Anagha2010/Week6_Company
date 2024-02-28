# Class definition
class Employee:
    # class constructor
    def __init__(self, emp_id, name, pronoun, role, salary):
        self.name = name
        self.emp_id = emp_id
        self.role = role
        self.salary = salary
        self.pronoun = pronoun

    # getter method to get value of attribute salary
    def get_salary(self):
        return self.salary

    # method to update salary for employee
    def update_salary(self, new_salary):
        if new_salary > 0:
            self.salary = new_salary
            print(f"\n{self.name}'s salary has been updated to {new_salary}.")
        else:
            print("Invalid salary. Please provide a positive value.")

    # The __str__() dunder method returns a reader-friendly string representation of class object.
    def __str__(self):
        return (f"\n{'*' * 20}\nEmployee ID: {self.emp_id}\nName: {self.name}\nRole: {self.role}\nSalary:"
                f" ${self.salary}\n{'*' * 20}")
