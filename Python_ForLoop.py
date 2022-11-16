#write a code to print numbers from 1 to 10

for i in range(1,11): #range(1,11) is a list which contains numbers from [1,2,3,4,....,9,10]
    print(i)

#write a code to print numbers from 1 to 10 using 2 steps
#Example to print odd numbers starting from value 1
for i in range(1,11,2):
    print(i)

#write a program to print numbers from 10 to 1
for i in range(10,0,-1):
    print(i)

#array is used to store homogeneous kind of data(single data type)
#list is used to store heterogeneous kind of data(any kind of data types)

#Write a program to calculate the sum of given list elements using for loop
a_list = [4,8,-2,10,5]
#output = 25
total = 0
for i in a_list:
    total += i
print(total)
