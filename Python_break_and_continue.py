#How to use break statement
int_list = [1,5,7,8,19,13,17,3]

#Find the even value in the given list
#a=[]
for i in int_list:
    print("Values in the list: ",i)
    if i%2==0:
        print("Even number in the list is: ", i)
        break

#if break is removed entire list will be checked
int_list = [1,5,7,8,19,13,17,3]
for i in int_list:
    print("Values in the list: ",i)
    if i%2==0:
        print("Even number in the list is: ", i)

#How to use continue keyword
#Print the numbers from for loop and start them from value 1
#But print values on terminal if number is greater than 10
for i in range(1,21):
    if i<10:
        continue
    print(i)
