#Numerical operators in Python
# + for addition, - for substraction, * for multiplication, / for float division,
# // for integer division, ** for power calculation, % for Modulus


x=6
y=3
print('Addition of x+y= ', x+y)
print('Substraction of x-y= ', x-y)
print('Multiplication of x*y= ', x*y)
print('Float division of x/y= ', x/y)
print('Integer division of x//y= ', x//y)
print('Power calculation of x**y= ', x**y)
print('Modulus of x%y= ', x%y)

#Some operators on string
str_val = 'Abhi'

# + is a concat operator on strings, -, *, / and any other operators won't work
Full_name = str_val + ' '+ 'Varshini'
print("Full Name=", Full_name)

#Multiply_name = 'Varshini'*3
#print("Full Name=", Multiply_name)

#Assignment operators
# -+, +=, -=, *=, /=, //=, %=

#Comparison Operators
# ==, Equals to condition, x==y
# !=, Not equals to condition, x!=y
# >, Greater than condition, x>y
# <, Less than condition, x<y
# >=, Greater than and equals to condition, x>=y
# <=, Less than and equals to condition, x<=y

a=10
b=5
print("Result of a==b , ", a==b)
print("Result of a!=b , ", a!=b)
print("Result of a<b , ", a<b)
print("Result of a>b , ", a>b)
print("Result of a<=b , ", a<=b)
print("Result of a>=b , ", a>=b)

#Logical operators(Logical check will happen for expression result)
#and -> Returns true if both the statements are true
#or -> Returns true if one of the statements are true
#not -> Reverse the result, returns false if the result is true and vice versa


m = 10
n = 8
print("m>10 and n<10 Result ", m>10 and n<10) #False
print("m>20 or n<10 Result ", m>20 or n<10) #True
print("not(m>20 and n<10) Result ", not(m>20 and n<10)) #True
