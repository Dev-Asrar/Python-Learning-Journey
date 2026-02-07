# WHILE LOOPS...

count=1
while count <= 100:
    print(count ,"Hello")
    count+=1

#Print numbers from 1 to 5...
i = 1
while i <= 5:
    print(i)
    i += 1
print("lOOP ENDED")

#Print numbers from 5 to 1 .....

i=5
while i >=1:
    print(i)
    i -= 1
print("LOOP ENDED")

#PRACTICE QUESTIONS.....
i = 1
while i <= 100:
    print(i)
    i += 1
print("LOOP ENDED")


i = 100
while i >= 1:
    print(i)
    i -= 1
print("LOOP ENDED")

n = int(input("Enter your number:"))
m = 1
while m<=10:
    print(n*m)
    m += 1
print("Multiplication of",n,"table ended.")

nums = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1

nums = (1,4,9,16,25,36,49,64,81,100)

i = 0
x= 81
while i < len(nums):
    if(x==nums[i]):
        print("found at index =",i)
    i += 1

# Break in loops...
i=1
while i <= 5:
    print(i)
    if(i == 4):
        break
    i += 1

#Continue in Loops ....

i = 1
while i <=10:
    if(i%2 == 0):
        i+=1
        continue
    print(i)
    i+=1