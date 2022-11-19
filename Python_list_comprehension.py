#Write a program to generate list of 10 numbers
result = []
for i in range(1,11):
    result.append(i)
print(result)

#How to do it with the help of list comprehension?
result = [x for x in range(-1,15)]
print(result)

#Get a list of all even numbers between 1 to 50
result = [x for x in range(1,51) if x%2 == 0]
print(result)

#Get a list of all even numbers from the input list
list_a = [2,4,3,6,7,5,12,10]
result = [x for x in list_a if x%2 == 0]
print(result)

#Convert all string into upper case in given list
list_a = ['hi', 'hello', 'hey', 'nice']
result = [x.upper() for x in list_a ]
print(result)

#Put all negative numbers after positive numbers from given list 
list_b = [1, -1,2,-5,9,10,-6]

#result = [1,2,9,10,-1,-5,-6]
result1 = [x for x in list_b if x>0]+[x for x in list_b if x<0]
print(result1)
