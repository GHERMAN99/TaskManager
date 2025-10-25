variables
from contextlib import nullcontext
from enum import member

integer = 10
flout = 9.8
string = 'Mosh'
boolean = False

#input == scanner
users_name = input('what is your name? ')
print('hi '+ users_name)

#to switch variables
birth_year = input ('birth year: ')
age = 2024 - int(birth_year)
print (age)

#to get the type of variables
type_of = 'brooo'
print(type(birth_year))

#string

basic = "hi world"
print(basic)
basic = '"hiii" world'
print(basic)


mail = '''
hi there,

python is ez

like no diffff

'''

print(mail)

basic = 'hi how are you'
print(basic[0])
print(basic[1])
print(basic[-1])
print(basic[-2])
print(basic[0:3]) # the last one in the range is not apart!!! in basic the print will be 'hi ' without the ''
print(basic[2:]) #from 2 to the end
print(basic[:5]) #from 5 to the start
the_same_as_basic = basic[:]
print(the_same_as_basic) #the print will be what ever is inside basic 'hi how are you'  without the ''


#formatted strings
first = 'guy'
last = 'herman'
msg = f'{first} [{last}] is a coder'
print(msg)

#string methodes
basic = 'Hi how are you'
print(len(basic)) # the amount of chars in basic
print(basic.upper()) # uppercase
print(basic.lower()) #lowercase
print(basic.find('o')) # the index of the closest o
print(basic.find('you')) # the first index of the world you
print(basic.replace('you','her')) # the print will be Hi how are her
print('you' in basic) # the answer will be a boolean type and the answer is true
print(basic.title()) # The title() method returns a string where the first character in every word is upper case for example the print will be Hi How Are You


#Arithmetic Operations
print(2 + 5) # 7
print(5 - 2) # 3
print(10 / 3) # 3.33333...
print(10 // 3) # 3
print (8 % 5) # 3
print(7 ** 2) # 49
'''all of the += is the same like java'''


# Math functions
x = 2.9
print(round(x)) # 3
x = -2.9
print(abs(x)) # 2.9

import math

print(math.ceil(2.9)) #3
print(math.floor(2.9)) #2
print(math.comb(2,4)) #Return the number of ways to choose k items from n items without repetition and without order. (2)
'''there are sooo much more'''


# if
is_hot = False
is_cold = True
if is_hot:
    print("it is a hot day")
    print("drink alot of water")
elif is_cold:
    print("it is not a hot day :(")
    print("dont go to the sea")
else:
    print("you are good to go")
print('have a good day :)')


#loghcal operation
# and == && in java
# or == || in java
# not == != in java
# we use the 'not' with "and not" and "or not"


#comparison operators
# > and >=
# < and <=
# ==
# !=


#while
#at the end of the while we while type ':'
#everything else is the same as java


#For loops
for i in 'dumb':
    print(i)
#the print will be
# d
# u
# m
# b

for i in ['guy' , 'maya' , 'noga']:
    print(i)
#the print will be
# guy
# maya
# noga

for i in range(5):
    print(i)
#the print will be
# 0
# 1
# 2
# 3
# 4

for i in range(5 , 10):
    print(i)
#the print will be
# 5
# 6
# 7
# 8
# 9

for i in range(5,10,2):
    print(i)
#the print will be
# 5
# 7
# 9

price = [10,20,30]
total_price = 0
for i in price:
    total_price += i;
print(f'the total price is {total_price}') # the total price is 60




#nested loops

# the coordinate ex
for x in range(4):
    for y in range(3):
        print(f"({x},{y})")
#run the shit to check the result

#print F
numbers = [5,2,5,2,2]
for x in numbers: # run traw numbers and saves the value
    output = ''
    for y in range(x):
       output += 'x'
    print(output)


#lists

names = ['Guy','Maya','Noga','Yoda']
print(names) # ['Guy', 'Maya', 'Noga','Yoda]

print(names[0]) # Guy
print(names[-1]) # Yoda
print(names[2:]) #['Noga', 'Yoda']

#how to find the max number in the list
numbers_list = [3,6,9,4,6,2,4]
max = numbers_list[0]
for i in numbers_list:
    if i > max:
        max = i
print(f'{max} is the biggest number is the list') #9 is the biggest number is the list


#2D list
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in matrix: #  row = list by place fot ex for the firs run on the loop row = [1,2,3]
    for item in row: # the item runs traw every thing in the list the row has for this point
        print(item)

#1
#2
#3
#4
#5
#6
#7
#8
#9



#list Methods

numbers_list = [5,4,3,2]
numbers_list.append(1) # now the numbers_list will have 1 at the end
print(numbers_list) # [5, 4, 3, 2, 1]

numbers_list.insert(0,6) # the first on is the index and the other one is the value
print(numbers_list) # [6, 5, 4, 3, 2, 1]
numbers_list.insert(3,7)
print(numbers_list) # [6, 5, 4, 7, 3, 2, 1]

numbers_list = [5,4,3,2,2] # remove the closest index with this value
numbers_list.remove(2)
print(numbers_list) # [5, 4, 3, 2]

numbers_list = [5,4,3,2]
numbers_list.clear() # clearing the list
print(numbers_list) # []

numbers_list = [5,4,3,2,2]
pop_value = numbers_list.pop() # the same pop as java
print(pop_value) # 2

numbers_list = [5,4,3,2]
print(numbers_list.index(5)) # give us the index of the value   0

numbers_list = [5,4,3,2]
print(7 in numbers_list) # False   we will get a boolean answer

numbers_list = [5,5,4,3,2]
print(numbers_list.count(5)) # 2  because we have 2 fives in the list

numbers_list = [5,4,3,2]
numbers_list.sort()
print(numbers_list) # [2, 3, 4, 5]
numbers_list.reverse()
print(numbers_list) # [5, 4, 3, 2]


numbers_list = [5,4,3,2]
numbers2_list = numbers_list.copy()
print(numbers2_list) # this is just a copy of numbers_list so the print will be [5,4,3,2]


# tuple
numbers_tuple = (1,2,3) # tup;e is list that you can not change
print(numbers_tuple[0]) # 1
# in tuple we only have count and index
#the index
numbers_tuple = (1,2,3)
print(numbers_tuple.index(1)) # give us the index of the value   0
#the count
numbers_tuple = (1,2,3)
print(numbers_tuple.count(1)) # 1  because we have 1 one in the tuple



#unpacking
coordinates = (1,2,3) # it can be [1,2,3] too
#insted of
#x = coordinates(0)
#y = coordinates(1)
#z = coordinates(2)
#we can unpack the tuple or list fpr exl
x,y,z = coordinates
print(x) # 1
print(y) # 2
print(z) # 3


#Dictionaries
customer = {
    "name": "Guy Herman",
    "age": "16",
    "know dictionaries": True
}
print(customer.get("name")) # Guy Herman
#you can add to the dictionaries for exl
customer["hair"] = "short"
print(customer.get("hair")) # short



# functions


def greet_user():
    print('hi there!')
    print('you are with me')

# after def some people do 2 tabs
greet_user()

#Parameters
def greet_user(name):
    print('hi there!' + name)
    print('you are with me')

# after def some people do 2 tabs
greet_user("Guy")

#keyword arguments
def greet_user(first_name,last_name):
    print(f'hi there! {first_name} {last_name}')
    print('you are with me')


# after def some people do 2 tabs
greet_user(last_name='Herman',first_name='Guy') # you can arrange the values in your order

#in python we have return or nothing(the nothing is void)
def f(num):
    print((num *num))


print(f(8)) # if we print a print the output will print None because if we print a print it is better to use return



#exception # lets say that we get string and not int but we dont wont the code to crash
try:
    age = int(input('age: '))
    print(age)
except ValueError:
    print('invalid value')
# we have more excepts like
# 'except ZeroDivisionError' when we divide by 0 the code will not crash




#classes  we can make all of the classes in one file
#the first letter of the class is with a capslock
class Dog:
    def __init__(self, age: int, color: str, owner: str): #in every def in the class we need to add the 'self' it is like this in java
        self.age = age
        self.color = color
        self.owner = owner

    def __repr__(self) -> str:  # the arrow is not needed   in python there more build in def but we do not have to use them
        return f"<Age: {self.age}, color: {self.color}, owner: {self.owner}>"

    def age_to_human(self):#in every def in the class we need to add the 'self' it is like this in java
        return self.age * 7


dog = Dog(2, "brown", "guy")
print(dog)
print(f"Human age: {dog.age_to_human()}")
dog.age += 1
print(dog)




#inheritance  ירושה we can make one class that other classes can use as their own class


class Mammal:
    def __init__(self, age: int, color: str, owner: str): #in every def in the class we need to add the 'self' it is like this in java
        self.age = age
        self.color = color
        self.owner = owner

    def __repr__(self) -> str:  # the arrow is not needed   in python there more build in def but we do not have to use them
        return f"<Age: {self.age}, color: {self.color}, owner: {self.owner}>"

    def age_to_human(self):#in every def in the class we need to add the 'self' it is like this in java
        return self.age * 7
# now we will make a class for dogs and a class for cats but because they have the same stuff we made only on big class and we inheritance the Mammal class to each one
class Dog(Mammal):
    pass
class Cat(Mammal):
    pass

dog1 = Dog(2,'black','Guy')
print(dog1.age_to_human()) # 14
cat1 = Cat(2,'white','Guy')
print(cat1.age_to_human())



#Modules  like classes in java
def lbs_to_kg(weight):
    return weight * 0.45

def kg_to_lbs(weight):
    return weight / 0.45
# if we want to us them in many files we while create a file with them and on the other files we will write import 'the name of the class that the defs are on'
# lets say that the name is Weight so we write at the top import weight and know we can do print(Weight.lbs_to_kg(weight))




#packages
#we open a python package and inside the packages we open files and then we can play with them



#Generating Random Values
import random
for i in range(3):
    print(random.random())
#we will get 3 random numbers from the range of 0 to 1

#let say we want a range from 10 to 20
for i in range(3):
    print(random.random(10,20))
#we will get 3 random numbers from the range of 10 to 20

# let say we want to use it to get a randon item in a list
con = True
i = 0
members = []
while(con):
    member[i] = input('give me a member')
    i += 1
    con = boolean.input('do you want to keep going? (answer in a boolean type)')
leader = random.choice(members)