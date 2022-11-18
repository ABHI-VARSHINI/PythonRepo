#Sets in Python

set1 = set() #empty set
print(type(set1))

set2 = {'Monday', 'Thursday', 'Monday'}
print(list(set2))

set4 = {1,2,3,4,5,6,1,5}
print(set4)

list1 = [1,2,3,4,1,2,3,4,5,6,7,8,1]
set3 = set(list1)
print(set3)

set5 = {}
print(type(set5))

#How we can iterate elements in the list
for i in set3:
    print(i)

#Convert output of set into list
list2 = [1,2,3,4,1,2,3,4,5,6,7,8,1]
set6 = list(list2)
print(list(set(set6)))
print(set6[::-1])

#How to insert elements in the set
set7 = set()
set7.add(11)
set7.add(12)
set7.add(11)
set7.add(1)
set7.add(13)
set7.add(13)
set7.add(3)
set7.add(11)
print(set7)

#Use of update method
tmp = [1,2,3,4,5,1,2,3,4,5,1,2,3]
set7.update(tmp)
print(set7)

#Calculate the lenth of the set
print(len(set7))

#Set operations
set_a = {1,2,3,4,5,6}
set_b = {3,6,8,9,10}

#Union operation
print("Union of two sets are: ", set_a | set_b)
print("Union of two sets are: ", set_a.union(set_b)) #another way of union by using union() function

#Intersection operation
print("Union of two sets are: ", set_a & set_b)
print("Union of two sets are: ", set_a.intersection(set_b))#another way of intersection by using intersection() function

#Difference between two sets
print("Difference between two sets: ", set_a - set_b)
print("Difference between two sets: ", set_b - set_a)

#Comparison in sets
set_x = {1,2,3,4,5}
set_y = {1,2,3,5,4,5,1}
print("Comparison in sets are: ", set_x == set_y)

set_m = {5,6,7,1,2,4}
print(set_m)

set_x = {1,2,3,4,5,6}
set_y = {1,2,3,5,4,5,1}
print("Comparison in sets are: ", set_x == set_y)
