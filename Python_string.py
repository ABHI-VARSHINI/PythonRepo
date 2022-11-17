#Create a string in python
str1 = "iNeuron"
print(str1)
print(type(str1))

str2 = "Varshi's"
print(str2)

str3 = "He is a 'good' boy"
print(str3)

#Printing lenth of the string by using lenth function
print("Length of the String is: ", len(str3))

#How to write multi-line string
str4 = '''Varsha is 
not going to 
attend the 
party'''
print(str4)
print(len(str4))

#String concatenation
str5 = "Varshu"
str6 = "Abhi"
print(str5+" "+str6)

#String comparision
str7 = "Varshu"
str8 = "Varshu"
print(str7==str8)

#How to print the each character from the string
for i in str7:
    print(i)

#How to print 4th letter in the string
print(str3[3])

str9 = "Akshitha"
#Update the 4th character(h) in the string by i
#str9[3] = "i" #TypeError: 'str' object does not support item assignment
#print(str9)

#Convert string into lower case
print("Lower case of the string is: "+str9.lower())

#Convert string into upper case
print("Upper case of the string is: "+str9.upper())

#Other functionalities will be same like list as slicing

