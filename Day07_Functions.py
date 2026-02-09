#FUNCTIONS......
def calc_sum(a, b):   #parameters
    sum=a+b
    print(sum)
    return sum

# After some lines of code..

calc_sum(66,34)    #function call;arguments

# Again after some lines of code...

calc_sum(12, 9)

# Again after some lines of code...

calc_sum(20, 9)

def print_hello():
    print("Hello world")

print_hello()
print_hello()
print_hello()

#Average of 3 numbers....
def average(a,b,c):
    avg=(a+b+c)/3
    print(avg)
    return avg

average(100,50,150)

#Built-in-Functions...

print("Lone","asrar",end=" ")
print("ul haq")
len()
type()
range()

#User-defined Functions....
# product of two numbers...
def multi(a=2,b=3):    #For default values give a&b seperate values here..
    product=a*b
    print(product)
    return product
multi()


nums = [4,3,6,2,7,5]
def length(list):
    print(len(list))
    return len
length(nums)

cities=["srinagar","tujjar","baramulla","sopore"]
length(cities)

def print_list(list):
    for item in list:
        print(item,end=" ")
        
print_list(cities)

def calc_fact(n):
    fact=1
    for i in range(1,n+1):
        fact *= i
    print(fact)
calc_fact(5)
calc_fact(100)

def converter(usd_value):
    inr_value=93*usd_value
    print(usd_value,"USD =",inr_value,"INR")
    return inr_value

converter(10760)

#Function for Even or Odd number...
num = int(input("Enter number:"))
def calc_form(num):
    if(num % 2 == 0):
        print("EVEN")
    else:
        print("ODD")
    return num

calc_form(num)

