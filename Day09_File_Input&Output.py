f = open("demo.txt","r")
data = f.read()

print(data)
print(type(data))
f.close()

data = f.read(10)   # prints ist characters...
print(data)

line1 = f.readline()  #prints whole line...
print(line1)

line2 = f.readline()
print(line2)

#write a letter...
f = open("demo.txt","a")     #Adds text at the end of the file...
f.write("\nThis is a sunny day & i don't want to stay at home. \nToday i can't do the writing portion.")

f = open("demo.txt","w")   #Deletes the ist text and rewrited the new one...
f.write("I have loved physics & math.\nBut chemistry didn't loved me. ")

#file in case of r+ mode..... starts erasing & rewriting from ist alphabit...
f = open("demo.txt","r+")
f.write("Asrar")
print(f.read())
f.close()

#file in case of w+....Erases the whole txt and then writes the given data...
f = open("demo.txt","w+")
f.write("Asrar")
print(f.read())
f.close()

#file in case of a+....Adds at the end of the text without erasing...
f = open("demo.txt","a+")
f.write("Lone")
print(f.read())

#With syntax....
with open("demo.txt","r")as f:
    data = f.read()
    print(data)

with open("demo.txt","w")as f:
    f.write("new words for same file.")

f= open("sample.txt","w")    #sample.txt file opened automatically...
f.write("I am the best")

# To delete a file....
import os
os.remove("sample.txt")

#PPROBLEM SOLVING......
#1
with open("practice.txt","w")as f:
    f.write("Hi Everyone\nWe are learning python I/O\nusing Java.\nI like programming in Java.")
    
#2
with open("practice.txt","r")as f:
    data = f.read()
    
new_data = data.replace("Java","python")
print(new_data)

with open("practice.txt","w")as f:
    f.write(new_data)

#3
def find_word():
    word = "learning"
    with open("practice.txt","r")as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("Not Found")

find_word()

#4
def check_line_no():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt","r")as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1       

check_line_no()

#5
count = 0
with open("practice.txt","r")as f:
    data = f.read()
    print(data)

    num = data.split(",")
    for val in num:
        if(int(val)%2 == 0):
            count+=1

print(count)          

