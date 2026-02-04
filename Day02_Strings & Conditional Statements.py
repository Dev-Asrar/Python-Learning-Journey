str1="I am in Love with a fairy tale. Even though it hurts"
str2="I am in Love with a fairy tale.\nEvev though it hurts" # \n :- for next line in str.
print(str1)
print(str2)

# CONCATENATION (addition of str)
str1="Lone"
str2="Asrar"
print(str1+str2)

# Length of str
str1="Tujjar sharief"
print(len(str1))

# INDEXING
str1="Jammu and Kashmir"
print(str1[3])

# SLICING
str1="This college is fantastic."
# print(str1[0:4])
print(str1[5:])
print(str1[:4])
print(str1[-10:-1])  #(negative slicing)

# STRING FUNCTIONS
str="python is a great language."
print(str.endswith("age."))

print(str.capitalize())

print(str.replace("python","javaseript"))

print(str.find("great"))

print(str.count("a"))

PRACTICE QUESTIONS....

name=input("Enter your name :")
print(len(name))


str="Hi, i am $ the big $& also the skinny $ and also $ollar man."
print(str.count("$"))

# CONDITIONAL STATEMENTS
age=9
if(age>=18):
    print("can Drive.\ncan vote.")
elif(age<18):
    print("YOU CAN N0T DO ANYTHING ")    

light = "pink"
if(light=="green"):
    print("GO!!!")
elif(light=="red"):
    print("Stop")
elif(light=="yellow"):
    print("Be Ready")
else:
    print("light is broken.")


marks=int(input("Enter your marks:"))
if(marks>=90):
    Grade = "A"
elif(marks>=80 and marks<90):
    Grade = "B"
elif(marks>=70 and marks<80):
    Grade = "C"
else:
    Grade = "Bhai Padh lai yeh koie Marks hai kya ????"
print("Grade of the student :->", Grade)

# NESTING....
age=int(input("Enter your age:"))
if(age>=18):
    if(age > 60):
        print("Sorry you are too old.")
    else:
        print("You are eligible for the Business.")
else:
    print("Abhi bacha hai tou , jaa kay POGO daikh .")

# PROBLEM SOLVINGGG.....

num=int(input("Enter your number:"))
if(num % 2 == 0):
    print("Its Even number.")
else:
    print("Ohh ODD one")


x = int(input("Enter ist number:"))
y = int(input("Enter 2nd number:"))
z = int(input("Enter 3rd number:"))
a = int(input("Enter 4th number:"))
if(x>=y and x>=z and x>=a):
    print("Ist is the Greatest number BOSS.")
elif(y>=z and y>= a):
    print("2nd is the Greatest number BOSS.")
elif(z>=a):
    print("3rd number is Greatest BOSS.")
else:
    print("4th number is the greatest BOSS.")