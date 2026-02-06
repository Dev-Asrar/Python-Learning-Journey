info ={
    "key":"value",
    "name":"Asrar",
    "age":19,
    "marks":90.9,
    "is_young":True,
    "subjects":["physics","chemistry","math","Biology","english"],
    9.00:61
}

print(info)
print(type(info))
print(info["subjects"])

info["name"]="Lone asrar"
info["surname"]="Lone"
print(info)

# NESTED DICTONARY....

student={
    "name":"Lone Asrar",
    "subjects":{
        "phy":98,
        "che":49,
        "math":84

    } 
}

# print(student)
print(student["subjects"]["che"])

#DICTONARY METHODS....
print(len(list(student.keys())))

print(len(list(student.values())))

lst= list(student.items())
print(lst[1])

print(student.get('name'))
print(student.get("name2"))  #gives NONE instead of error.

new_dict={"age":19,"city":"tujjar sharieff"}
student.update(new_dict)
print(student)

# SETS.....
collection={1,3,4,6,4,"Lone","Asrar","Lone"}
print(collection)
print(type(collection))
print(len(collection))

# EMPTY SET...

collection=set()
print(type(collection))

#SET METHODS.....
collection= set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add("Lone")
collection.add("Asrar")
collection.remove(2)
collection.add((1,2,3,4,5))

print(collection)
print(list(collection))

collection.clear()
print(len(collection))

collection={1,5,9,"Asrar","Tujjar","munsha",}

print(collection.pop())
print(collection.pop())

# SET UNIONS AND INTERSECTIONS.....

set1= {1,2,3,4,"Asrar","Unknown"}
set2={7,4,2,"Asrar",0,2,4,"Known"}

print(set1.union(set2))
print(set1.intersection(set2))

# PROBLEM SOLVINGGG....

dic={
    "cat":"A small animal",
    "table":["A piece of furniture","list of fact and figures"]
}
print(dic)

subjects={"python","java","c++","python","javascript","java","python","java","c++","c"}
classrooms_reqd=len(subjects)
print(classrooms_reqd)

dict={}
a=int(input("Enter Math's marks:"))
dict.update({"math":a})
b=int(input("Enter Phy's marks:"))
dict.update({"phy":b})
c=int(input("Enter che's marks:"))
dict.update({"che":c})


print(dict)

values={
    ("float",9.0),
    ("int",9)
}

print(values)