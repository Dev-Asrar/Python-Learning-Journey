print("Hello World") 
print("You know nothing,","Jon Snow.")
print("We can print Anything.")

print(9)
print(77+23)
print(55-25)

#VARIABLES

name="Asrar"
age=19
aura=9999.99
old=False
degree=None

print("My name is:",name)
print("My aura is:",aura)
print("My age is:",age)
print("Am I old:",old)
print("Have I any degree:",degree)

print(type(name))
print(type(age))
print(type(aura))
print(type(old))
print(type(degree))

# COMMENTS (Code which does not execute)
 
# print("Hello World")
"""Python is a great language,
extraordinary one. I started this officially on 03 feb 2026."""

# ARITHIMETIC OPERATORS

a=10
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #remainder
print(a**b) #a^b

# RELATIONAL OPERATORS (Gives True/False as answer)
a=20
b=10
print(a==b)
print(a!=b)
print(a>=b)
print(a>b)
print(a<=b)
print(a<b)

# ASSIGNMENT OPERATORS
num = 10

num += 5
num -= 5
num *= 5
num /= 5
num **= 5
num %= 5
print(num)

# LOGICAL OPERATORS 
a = 100
b = 1
print(not(a>b))
print(not True)

val1= True
val2= False
print("AND operator:",val1 and val2)
print("OR operator:",val1 or val2)

# TYPE CONVERSIONS
a = int("4")
b = 2.5
print(a+b)

c = 3.14
c = str(c)
print(type(c))

# INPUTS
name = input("Enter your name:")
age = input("Enter age:")
height = input("Enter height:")

print("Welcome",name)
print("Aged:",age)
print("Mentioned height:",height)

# PRACTICE QUESTIONS

num1= int(input("Enter ist number:"))
num2= int(input("Enter 2nd number:"))
print(num1 + num2)

a = int(input("Enter side of the square:"))
print("Area of square=",a*a)
