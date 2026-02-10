#RECURSION.....
def show(n):  
    if(n==0):      #Conditional statement = Base case
        return
    print(n)
    show(n-1)

show(10)

def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1)* n
    

print(fact(5))

#PROBLEM SOLVING......
def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n

print(sum(15))

cities = ["srinagar","sopore","tujjar","nandpora","baramulla"]
def show(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    show(list,idx+1)
    

show(cities)