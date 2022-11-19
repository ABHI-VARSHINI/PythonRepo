#How to create a class in python
class Employee:

    #Constructor to a class
    #It is mainly used for assignment of instance variables
    def __init__(self, name, salary): 
        #self is the pointer to class
        #instance variable or instance attributes
        self.emp_name = name
        self.emp_salary = salary

    #method of a class
    def displayEmployeeInfo(self):
        print("Employee name: =", self.emp_name)
        print("Employee salary is: =", self.emp_salary)

emp1 = Employee('Abhi', 5678909) #emp1 is object
emp2 = Employee('Varshi', 567)
emp1.displayEmployeeInfo()
emp2.displayEmployeeInfo()

print(emp1.emp_name)
print(emp2.emp_salary)

#Difference between class and instance variable
