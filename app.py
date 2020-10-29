
#print statement
print("Hello World!")
#VARIABLE TYPES : int, float, str, bool. Three types of data : numbers, strings, boolean
price = 19.95
age = 20
first_name = "Mosh"
is_online = False #False and True are keywords and begin with a capital letter. As python is case sensitive.
#EXERCISE 1
name = "John Smith"
age = 20
is_new = True

#Receiving input
input("What is your name? ") #the space after the question mark separates the cursor from the question mark indicating that there may be an input to be read.
#the input() returns the value entered in the terminal window.

name = input("What is your name? ")
print("Hello " + name)

#type conversion
birth_year = input("Enter your birth year: ") #the input() returns a value as string. if I enter 1994 as my input, the func returns as "1994"
age = 2020 - int(birth_year)
print(age)
#type conversion built in functions:
#int() - to convert a value into an integer.
#float() - to convert a value into a float.
#bool() - to convert a value into a boolean.
#str() - to convert a value into a string.

#exercise 2

num1 = input("First : ")
num2 = input("Second: ") #if u just give num1 + num2 then if num1=10 and num2=20; printing sum will give : "1020"
sum = float(num1) + float(num2)
print("Sum : " + str(sum)) #python cant concatenate a str with a float or int....."Sum : " + 19.95------x

#all are objects in python. String is an object in python and this has many methods.
#find('y') or find("for") - returns the index of the first occurence of the element, replace(), upper(), lower()
#use of in keyword.

course = "Python for Beginners"
print("Python" in course) #prints true in the terminal.

#arithmetic operators
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3) #gives a decimal ans.
print(10 // 3) #gives an int ans.
print(10 % 3) #gives a remainder.
print(10 ** 3) #gives an exponential.

#augmented operators.
#x = 10
#x = x + 3 can be written as x+=3

#comparision operators
#>, >=, <, <=, ==, !=

#3 logical operators:
#and - both expressions return true.
#or - at least one expression returns true.
#not - inverses the value given

#if statements
temperature = 3
if temperature > 30:
    print("It's a hot day")
elif temperature > 20: #(between 20 and 30)
    print("It's a nice day")
elif temperature > 10: #(between 10 and 20)
    print("It's a bit cold")
else:
    print("It's cold")
print("Done")

#Exercise

weight = float(input("Weight: "))
weight_type = input("(K)g or (L)bs: ")

if weight_type == "K" or weight_type == "k":
    new_weight = weight * 2.205
    print("Weight in Lbs: " + str(new_weight))
elif weight_type == "L" or weight_type == "l":
    new_weight = weight / 2.205
    print("Weight in Kg: " + str(new_weight))

#I think it s not nice to stop with a elif rather than an else.

#Solution
weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K": #the upper() returns a new string other than the original string, be it "k" or "K"
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))

#while loops
i = 1
while i <= 5:
    print(i)
    i = i + 1 #increment has to be there, if not i will always be 1 and the loop will run infinitely. Basically the program runs untill it runs out of
    #memory.

#u cn easily print 1 to 1000
i = 1
while i <= 1_000: #we have an underscore to make the number more readable.
    print(i, end="")
    i += 1

#printing an expression
i = 1
while i <= 10:
    print(i * "*") # in python, u cannot concatenate a string with a number but you can multiply a string with a number. Here it ll repeat the "*"
    #according to the i value.
    i += 1

#printing an inverted triangle
i = 10
print(" ")
while i >= 1:
    print(i * "*")
    i -= 1

#There are complex data types in python
# 1. LISTS - represented within []
#USE LISTS WHEN WE HAVE TO REPRESENT A LIST OF OBJECTS :E.G A LIST OF NUMBERS OR LIST OF NAMES.
names = ["John", "Bob", "Mosh", "Sam", "Mary"]
print(names)
#to access individual elements in the list.
print(names[0])

#python uses negative index.
print(names[-1]) #this prints the last element in the list.
print(names[-2]) #this prints the second last element in the list.

#change the element in a particular index. We have to reset it to a new value.
names[0] = "Jon"
print(names)

#selecting a range to display certain names
print(names[0:3]) #does nt modify the existing list but returns a new list.
print(names)

#List methods
# 1. append()
numbers = [1, 2, 3, 4, 5]
numbers.append(6) #add an element at the end of the list.
print(numbers)

#2. insert()
numbers.insert(0, -1) # 0 is the index in the list where you want to change. -1 is the element u added.
print(numbers)

#3. remove()
#if u want to remove an element from the list.
numbers = [1,2,3,4,5]
numbers.remove(3) #here 3 is the value in the list and not the index of the value.
print(numbers)

#4.clear()
#if u want to remove all the elements in the list.
numbers.clear() #does nt expect any parameters.
print(numbers)

#to find if an item exists in a list or not.
# using "in" operator
numbers = [1,2,3,4,5]
print(1 in numbers) # this is a boolean expression and thus returs a boolean value.

#5. len() - a built in function like print() and thats why it is purple.
#to find out how many items in the list.
print(len(numbers))

#for loops
for item in numbers: #item is the loop variable which changes value during the loop.
    print(item) #item variable takes a value in the list in each iteration.

#if we use a while loop for this:
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

#the range function
#using the range function to generate a sequence of numbers.
numbers = range(5) #this will return a range object. A range object that can store a sequence of objects. This returns the default format for range object
#which is range(0, 5)
#print(numbers)
#iterate over a range object.
for number in numbers:
    print(number)
    i += 1 #this will print the numbers specified in the range 0 to 5; 0, 1, 2, 3, 4

numbers = range(5, 10) # range is 5 to 10.
for number in numbers:
    print(number)
    i += 1

numbers = range(5, 10, 2) # incremented by 2
for number in numbers:
    print(number)

#we dont need to hold the range object in a separate variable "numbers" when using with for loop.
for number in range(5, 10):
    print(number)

#tuples - they are immutable, we cannot change them after we create them. used to store a sequence of objects.
numbers = (1,2, 3, 3) #use parenthese to represent tuples.
#numbers[0] = 10 //cant reassign since tuples are immutable.

numbers.count(3) #count returns a number of occurences of the element specifies as parameter in the count method.
numbers.index(3) #index of the first occurence of the element.

#the tuple methods that start with an underscore are magic methods.
