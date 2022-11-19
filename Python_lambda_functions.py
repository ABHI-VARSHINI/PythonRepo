#How to create lambda functions

#First normal function to add integer 5 in given number

def add_five(num):
    result = num+5
    print(result)
add_five(6)

#Same program using lambda function
lambda_add_five =  lambda x : x+5
print("Result is", lambda_add_five(10)) #we need to pass x value in the argument

#lambda function to add two input numbers
lambda_add_two_nums = lambda x,y : x+y
a=5
b=6
print("Sum of two numbers are: ",lambda_add_two_nums(a,b)) #We need to pass a,b as two arguments or we can give values to direct x and y

#Write a lambda function to concatenate two input strings
lambda_concat_twostrings = lambda x,y : x+y
print(lambda_concat_twostrings("Hey","Hi"))

#Write a lambda function to calculate maximum of two numbers 
lambda_maxoftwo = lambda m,n : m if m>n else n
print(lambda_maxoftwo(6,7))

#How to work with map(), filter() and reduce()

