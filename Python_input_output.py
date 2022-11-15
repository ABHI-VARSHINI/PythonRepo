int_var = 568
float_var = 567678.54678
string_var = 'hey hii!!'
bool_var = False

#Printing the variables
print('Hello every1/!!')
print('Value of int variable is ', int_var, "okay")
print('Value of float variable is ', float_var, "result_done")
print('Value of string variable is ', string_var, "- printed")
print('Value of bool variable is ', bool_var, "- just practice")

#How to check variable type() the functions
print('Type of int variable is: ', type(int_var))
print('Type of float variable is: ', type(float_var))
print('Type of string variable is: ', type(string_var))
print('Type of bool variable is: ', type(bool_var))

#Type Casting
int_var = int_var+15
type_cast_int = float(int_var)
type_cast_float = int(float_var)
print('type casting from int to float', type_cast_int)
print('type casting from int to float', type_cast_float)

#str type cating to int
string_var1 = "562"
string_var1 = int(string_var1) + 21
print('String conversion', string_var1)

name = input("Enter value for name: ")
age = input("Emter value for age: ")
print("User name is: ", name)
print("User age is: ", age)
