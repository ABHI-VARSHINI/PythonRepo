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

#Implement map() function
list1 = [1,2,3,4,5,6,7,8,9]

#Result
#result = [1,4,9,16,25,36,49,64,81]

square_num = lambda sqr : sqr*sqr
square_list = map(square_num, list1)

print(list(square_list))

#Add sequential respective elements in two given list
list_a = [1,2,3,4,3]
list_b = [5,4,5,2,1]

#Result= [6,6,8,6,4]
add_sequential = lambda a,b : a+b
add_lists = map(add_sequential,list_a,list_b)

print("Addition of two lists: ",list(add_lists))

#Implement reduce() function
import functools #reduce() function is present inside reduce() function

list_x = [1,2,3,4,5]

add_two_nums = lambda x,y : x+y
result = functools.reduce(add_two_nums, list_x)
print(result)

#Multiply two nums
list_x = [1,2,3,4,5]

add_two_nums = lambda x,y : x*y
result = functools.reduce(add_two_nums, list_x)
print(result)

#How to use filter()
#Create list to filter odd elements
seq = [1,2,5,6,7,9,13]

filter_odd = lambda x : x%2!=0
result = filter(filter_odd, seq)
print(list(result))
