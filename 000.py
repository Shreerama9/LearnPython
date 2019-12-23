print("Hello World!")
print("--------- ")
print("--      --")
print("----------")
print("--       +--")

character_name = "Shreerama"
character_age = "17"
is_male = "true"




print(" " + character_name + " is " + character_age + " years old   ")

character_name0 = "Prashant"
print("" + character_name + " has a big brother known as " + character_name0  +  " ")


print("Shreerama\nBharadwaja")
# cancatination is create string on other string.

phrase = "SRSSBVS"
print(phrase + " is awesome ")


# function can be used to modify strings
phrase = "SRSSBVS"
print(phrase.lower())
print(phrase.upper())
print(phrase.islower())
print(phrase.lower().islower())
print(len(phrase))
print(len(phrase) + 2 )

print(phrase[1])
print(phrase[4])


# index =give no. of the space occupied by the given character
print(phrase.index("SR"))
print(phrase.replace("SSBVS","S"))
name = "   shreeraima  ,  Samriddhi  ,vivek,vikrant"
var = name.replace("," , "\n ")
print(var)
# phrase[0:n] is used to get alphabets in that phase from 0 to n.
print(phrase[2:6])
print(phrase[0:7])


#strip is used to remove space in name or phrase (as used ) between ""
pace = "     SR     "
print(pace.strip())
stri = "This is a good guy named "
print(stri + name)
stri = "This is a good guy named "
name1 = "son"
name2 = "Rohan"
stri2 = "and he has friend called  "
print(stri + name1 + stri2 + name2 )
temp = "this is my {} and and he is a good boy named {}.".format(name1,name2)
print(temp)
# they are 0 and 1 in brackets y default.
temp = "this is my {1} and and he is a good boy named {0}.".format(name1,name2)
print(temp)
temp = f"this is my {name1} and and he is a good boy named {name2}."
# f string is newly introduced string.
print(temp)


'''Python collections:
1. List
2.Tuple
3.Set
4.collection
'''

'''lst = [61,2,3,4,6,41]
var = type(lst)
class
var = lst[2]
var = lst[0:5]
'''
'''list method {google it}
lst.pop
lst.insert
lst.append(2000)
'''

#var = lst
#print(var)
'''
tuple and lst are simillar but tuple cannot be easily changed as lst.
Use google for functions.
'''

#set
s1 = {23,25,3,66,78,49,65,91,64,11}
#s1.add(5655)
#s1.update([444,555,6666,88888,999909999])
print(len(s1))
#s1.remove(3)
#s1.discard(11)
#intersection, union, del,.pop  and etc
print(s1)

#dictionary

harryDict = {
    "Name": "Harry",
    "Class": "4th",
    "Marks": 35.50,
    "Hours in Class": 6
}
print(harryDict)
print(harryDict["Marks"])
print(harryDict["Class"])
print(harryDict["Hours in Class"])
harryDict.pop("Marks")
print(harryDict)
#for more google it.


# list, tuple , dictionary, frozenset , set


# type() is used to give types of function used
age = 18;
age = 40.58585;
print(type(age))
number = 525
# casting in python
# multi word variable
number_and_age = (number * age)
print(number_and_age)

# list
our_list = ["a", "b", "c", 1.5]
print(our_list)

our_tuple = ('a', 'b', 'c')
print(our_tuple)

'''our_dictionary = {"shreerama","srssbvs","ramee","shree"}
print(our_dictionary)
'''
our_dictionary: dict[str, str] = {"key1": "value1", "key2": "value2"}
print(our_dictionary)


'''SET V TUPLE 
set is mutable 
i.e python object can be changed 
while tuple dont

EXAMPLE'''

list = ["apples","bananas","mangoes"]
list[0] = "grapppes"
print(list)


list = ["apples","bananas","mangoes"]
id(list)
print(id)


print(-23022.44844)
print(3+4.568)
print(3*4+5)
# without bracket prog will go ne by one)
print(100%3)
# % operator is known as modulus and give remainder#

my_num = 56
print(my_num)
# num become string by using str() and used in line

print(str(my_num) + " is my favorite number")
# abs() is used to get absolute number
my_num = -66
print(abs(my_num))

print(pow(5,2))

print(max(56, -5))

print(round(53.4545))

from math import *
print(floor(5.55))
print(ceil(5.5659))
print(sqrt(66))
print(pow(64,0.5))

#input is used to get input from the user
name = input("Enter your name :    ")
a = input("Enter a ="   )#b = input("Enter b ="   )

print("Hey "+ name + "!")


num1 = 2
num2 = 3
print(num1 + num2)


# type casting

e = "31"
e = 3.1456
print(type(e))
d = 3.999
print(type(d))
'''
e= "31"
print(e + 2)
cannot work as e is string now.
'''

e = "31"
e = int(e)
print(e+2)
# int is for defining presence of integer.

e = float(e)
print(e+2)

'''
e = str(e)
print(e+2)
will not work
'''


#** exponent division
#// floor division




# if and else.
'''



age = input("Enter your Age\n     ")
age = int(age)
#print(type(age))

if(age>18):
    print("You can Drive a car")
elif(age==18):
            print("Get your license and Enjoy")
else:
    print("You cannot drive a vehicle")

'''

#Loops
#u have to print 1 to 1000
for i in range(0, 1000):
    print(i)


for c in range(1, 11):
    print(c*2)

for a in range(0, 11):
    print(a*a)

li = [1,425,"this"]
for item in li:
    print(item)

'''quiz : use for loop to iterate dictionary , set and tuples '''

i = 0
while(i<200):
  print(i+10)
  if i== 120:
      break
i = i +10




i = 0
while (i<100):
    print(i+ 1)
    if i == 68:
        continue
    i = i + 1




from typing import Dict

x = 1
if x < 0:
    print("x is less tha 0")
else:
    print("x is greater than 0")
    
    
    
#for loop

name = "Shreerama Shiva Sai Bharadwaja"
for element in name:
    print(element)


list_a =["shreerama","deepak","88211"]
for name in list_a:
    print(name)
n = int(input())
m = int(input())
g = int(input())
list_q = [n,m,g]
for number in list_q:
    print(number)
    
