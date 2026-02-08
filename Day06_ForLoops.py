# FOR LOOPS....

collection = ["apple","Banana","Civic sense","Dal"]
for ele in collection:
    print(ele)

tup = (1,4,3,2,6,4,6,5)
for num in tup:
    print(num)


str = ("Lone Asrar")
for chr in str:
    print(chr)

str = ("Tujar is a beautiful place.")
for chr in str:
    if(chr == 'j'):
        print("j found")
        break
    print(chr)
print("code ended")

# PROBLEM SOLVING...

list = [1,4,9,16,25,36,49,64,81,100]
for ele in list:
    print(ele)

tup = (1,4,9,16,25,36,49,64,81,100,81)
x = 81
idx = 0
for ele in tup:
    if(ele == x):
        print("Found in place =", idx+1)
    idx +=1

# FUNCTION(RANGE)...

print(range(5))

seq = range(5)
for ele in seq:
    print(ele)

for ele in range(5):
    print(ele)

seq = range(5)
print(seq[4])

for ele in range(10):  #(stop)
    print(ele)

for ele in range(2,10): #(start , stop)
    print(ele)

for ele in range(2,10,2): #(start, stop, step)
    print(ele)

for ele in range(1,100,2):
    print(ele)

# PRACTICE QUESTIONS...

for ele in range(1,101):
    print(ele)

for ele in range(100,0,-1):
    print(ele)

# TABLE OF N.....
n = int(input("Enter number :"))
for ele in range(1,11):
    print(n*ele)

#EMPTY LOOP...

for ele in range(5):
    pass
print("Empty loop created successfully")

# Sum of n numbers...
n = 20
sum = 0
for i in range(1,n+1):
    sum += i
print("sum total=",sum)

n=20
sum=0
i = 1
while i <=20:
    sum += i
    i += 1
print("Sum total = ",sum)

#Factorial of n ...

n = int(input("enter number:"))
fact = 1
for i in range(1,n+1):
    fact *= i
print("Factorial = ", fact)

n = 5
fact = 1
i = 1
while i <= 5:
    fact *= i
    i += 1
print("Factorial =",fact)

