#How to create a class in python
class Employee:
    #class attribute
    empCount = 0

    #Constructor to a class
    #It is mainly used for assignment of instance variables
    def __init__(self, name, salary): 
        #self is the pointer to class
        #instance variable or instance attributes
        self.emp_name = name
        self.emp_salary = salary
        Employee.empCount += 1

    #method of a class
    def displayEmployeeInfo(self):
        print("Employee name: =", self.emp_name)
        print("Employee salary is: =", self.emp_salary)
    def EmloyeeCount(self):
        print(("Employee count: ", Employee.empCount))

emp1 = Employee('Abhi', 5678909) #emp1 is object
emp1.EmloyeeCount()
emp2 = Employee('Varshi', 567)

emp1.displayEmployeeInfo()
emp2.displayEmployeeInfo()

emp2.EmloyeeCount()

#Print instance variables of a object
print(emp1.emp_name)
print(emp1.emp_salary)

#Let's access class variable from instance itself
print(emp1.empCount)
print(emp2.empCount)

emp1.empCount = 10
emp2.empCount = 20

print(emp1.empCount)
print(emp2.empCount)
print(Employee.empCount) #it will return number of instance(objects)

#What is static method in python?
class Car:
    def __init__(self, name, color):
        self.car_name = name
        self.car_color = color
    
    def displayCardetails(self):
        print("car name is: ", self.car_name)
        print("Car color is: ", self.car_color)
    
    @staticmethod
    def intialMessage():
        print("Hey, welcome to static method")

print(Car.intialMessage())

car1 = Car('XUV 700', 'Red')
car1.displayCardetails()

#This will not work
#Car.displayCardetails()

#Deloitte Company
class Employee:
    @staticmethod
    def isEmployeeOf():
        print("I am an employee of Deloitte")

Employee.isEmployeeOf()

#Add two nums using static method
class Calculation:
    @staticmethod
    def addTwoNums(num1, num2):
        print("Sum of two numbers is: ", num1+num2)

Calculation.addTwoNums(8, 3)
