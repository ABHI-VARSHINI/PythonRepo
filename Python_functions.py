#Functions in python
#What about len() 

list1 = [1,2,3,4,5,6]
print("Maximum number from the list is: ",max(list1)) #max() is inbuilt function in python
print("Maximum number from the list is: ",min(list1))
print("Sum the list is: ",sum(list1))

#How do function works
#They may or may not accepts input parameters
#They may or may not return any output

#Example of a function which doesn't accept any parameter
#and doesn't return anything
def welcome_message():
    print("Hey, hii")
welcome_message()

#Example of a function which doesn't accept any parameter
#and does return something
def bot_message():
    print("message from bot !!")
    return "Functions concept!!"
    
print(bot_message())
result = bot_message()
print("Bot result is: ", bot_message())

#Example of a function which accepts some parameter and return the values
def avg_of_two_nums(num1):
    print("message from bot !!")
    return "Functions concept!!"
    
print(bot_message())
result = bot_message()
print("Bot result is: ", bot_message())

#Example of a function which accepts some parameter and return the values
def avg_of_two_num(a, b):
    print("First value is: ",a)
    print("Second value is: ",b)
    avg_rslt = (a+b)//2
    return avg_rslt
output = avg_of_two_num(6, 2)
print("Average value is: ",output)

#Write a function to calculate the factorial of a number

def factorial(n):
    if n==0 | n==1:
        return 1
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
print("Factorial of the given number is: ",factorial(10))

#How to return multiple values from function
a, b, c = 7, 8, 6
print("Value of a is: ", a)
print("Value of b is: ", b)
print("Value of c is: ", c)

def square_and_cube(n):
    sqrt = n*n
    cube = n*n*n
    return sqrt, cube
print("Square and cube of the given number is: ", square_and_cube(5))
num=6
sqr_num, cube_num = square_and_cube(num)
print("Square root of ",num, "is: ", sqr_num)
print("Cube root of ",num, "is: ", cube_num)

#How to create optional arguments in python functions
#def multiply(a=3, b): #not possibe
def multiply(a, b=6):
    result = a*b
    return result
num1=10
num2=3
print("Multiplication of the two numbers are: ", multiply(num1, num2))
print("Multiplication of the two numbers are: ", multiply(num1))
print("Multiplication of the two numbers are: ", multiply(num2))

def multiply(a, b=6, c=4):
    result = a*b*c
    return result
num1=10
num2=3
num3=2
print("Multiplication of the three numbers are: ", multiply(num1, num2,num3))
print("Multiplication of the three numbers are: ", multiply(num1,num3))
print("Multiplication of the two numbers are: ", multiply(num2,num1))

#Non-key valued arguments
def example_nonkeyed_args(*argv):
    for param in argv:
        print(param)
example_nonkeyed_args('hey', 'hii',4,5,5678.45678)

#key value type of arguments in python
def example_of_kwargs(**kwargs):
    print("V")
    for k, v in kwargs.items():
        print("Key is: ", k, "value is: ",v)
example_of_kwargs(host='170.80.80.80', port=9021, pwd='DFJHMNB')
