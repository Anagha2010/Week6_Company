# imports
from Company.employee import Employee
from Company.company import Company

# Instantiating Employee objects
employee1 = Employee('001', 'Patty', "she", "Owner", 200000)
employee2 = Employee('002', "Tom", "he", "Senior Lawyer", 100000)
employee3 = Employee('003',"Ellen", "she","Lawyer", 50000)

# Instantiating object of Company class
company = Company("Hewes & Associates")

# Calling hire_employee method on objects of Company class
company.hire_employee(employee1)
# prints object - represented in a user-friendly way
print(employee1)
company.hire_employee(employee2)
print(employee2)
company.hire_employee(employee3)
print(employee3)

company.list_employees()

# printing salary using getter method of Employee class
print(employee3.get_salary())

# Calling update_salary method from Employee class on Employee class instances
employee3.update_salary(75000)
employee2.update_salary(150000)
employee1.update_salary(250000)

# methods from company class
company.fire_employee(employee1)
company.fire_employee(employee2)

# printing again for latest modified list
company.list_employees()
