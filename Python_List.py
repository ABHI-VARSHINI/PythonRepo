#Declare empty list
L1 = []
print(type(L1))

#Insert values in list
L1.append(5)
L1.append(8)
L1.append(11)
print(L1)

#Create a list of 1000 numbers starting from 1 to 1000
int_list = []
for i in range(1,1001):
    int_list.append(i)
print(int_list)

#How to calculate the length of a list
length_of_list = len(int_list)
print("Length of the list is: ", length_of_list)

list1 = [2, 12.5, "Abhiva", 5]
list2 = [2, 12.5, "Abhiva", 5.1]
print("Given two lists are equal? ", list1 == list2)

list3 = [4, 53, 124, 6789, 578.65]
list4 = [5678, "varsh", 67, "sj7"]
list5 = list3 + list4
print(list5)

#print all the elements of given list
for i in list4:
    print(i)

#print 3rd element of given list
list6 = [10, 15, 20, 25, 30, 35]
print("Third element in the given list is: ", list6[2])

#what will happen if you print 100th value in the array which doesn't exist
#print(list6[100]) #It will throw an error:-> IndexError: list index out of range

list7 = [1, 2, "Abhi", 1000]
print(list7)
#how to update the value of list index item?
#Update Abhi to Varsha
list7[2] = "Varsha"
print(list7)

#How to print list elements using length?
for i in range(0, len(list7)):
    print("Values in the list are: ", list7[i])
#list in list
list8 = [3, 4, 6, "Abhi", 9, "Varshu"]
print("Length if list8 is: ", len(list8))

#Difference between append and extend
list9 = [20, 30, 10]
list10 = ["hey", "varshi", "hii"]
print(list9)
print(list10)
list9.append(list10)
print("Appended list result is: ", list9)
print("Length after append: ", len(list9))

list11 = [20, 30, 10]
list12 = ["hey", "varshi", "hii"]
list11.extend(list12)
print("Extended list result is: ", list11)
print("Length after append: ", len(list11))

#List slicing
#End index is always exclusive
list13 = [10, 20, 30, 50, 60, 40, 90, 70, 80]
print(list13[0:7])
print(list13[4:8])
print(list13[7:11])
print(list13[:])
print(list13[0::2]) #3rd value is for step which is used to skip the value

#How to print last value of the list
print(list13[-1])

#How to print second last value of the list
print(list13[-2])

#How to print input list in reverse direction
print(list13[::-1])
