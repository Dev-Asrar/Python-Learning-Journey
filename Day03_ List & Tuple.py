marks=[88.9, 89.5, 45.9, 99.9]
print(marks)
print(type(marks))
print(len(marks))
print(marks[2])

student= ["munsha", 96, 18, "Dil"]
print(student[0])
student[0]="mannu"
print(student)
print(student[0])

# SLICING IN LISTS....
age= [14, 24, 45, 23, 11]
print(age[1:3])
print(age[-5:-1])

# LIST METHODS...
list= [5,6,2,3,1,4]
list.append(7)
print(list)

list.sort()    #in acending order...
print(list)
print(list.sort())
print(list)

list.sort(reverse=True)  #in decending order...
print(list)

list.reverse()  #reverses the whole original list...
print(list)

list.insert(4,"asrar")
print(list)

list.remove(3)
print(list)

list.pop(0)
print(list)

#TOUPLES.....
tup=(3,5,1,7,5,)
print(type(tup))
print(len(tup))
print(tup[0])

tup=(1,)  #if only one element is in tuple then after the element the ",(comma)"is must usedd...
print(type(tup))
print(len(tup))
print(tup[0])

#SLICING....
tup=(1,3,5,8,74,3,)
print(tup[1:4])
print(tup[-3:-1])

tup=(7,3,5,44,53,22,85,22,)
print(tup.index(44))
print(tup.count(22))

#PROBLEM SOLVINGGGG.....
movies=[]
a=input("Enter ist fovourite movie:")
b=input("Enter 2nd favourite movie:")
c=input("Enter 3rd favourite movie:")

movies.append(a)
movies.append(b)
movies.append(c)
print(movies)

list1=[1,2,3,4,5]
list2=list1.copy()
list2.reverse()
if(list1==list2):
    print("It's a Pallindrome")
else:
    print("NOT Palindriome")

tup=("C","D","A","A","B","B","A")
print(tup.count("B"))