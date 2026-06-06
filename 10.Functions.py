"""
Topic: Functions
Author: Poojan
Description: Basic examples of Functions.
""" 

"----------------------------------------------------------------------------------------------------------------"
"---Functions---"
# Functions means reusable code into a block that can be executed by calling the function name.

# There are many in-built functions in python like - print(), input() len() etc.
# we can create our own function also.

def poojan():                   #def is used to create function.              
    print("My name is Poojan") 

poojan()            #use of function.

"---Function Parameter and arguments---"

# parameters are variable listed inside the function definition.
# arguments are value passed to a function when it is called. 

def name(yourname): #your name is a parameter
    print(f"hello,{yourname}!")

name("poojanThummer")

"----------------------------------------------------------------------------------------------------------------"
"---Types of argument---"

# positional argument
# keyword argument
# default argument

"---Positional argument---"

def add(a,b): 
    return a+b

print(add(9,9)) # positional argument

"----------------------------------------------------------------------------------------------------------------"
"---keyword argument---"

def intro(name,age):
    print(f"I am {name} and I am {age} years old.")

intro(age=23,name="poojan") #keyword argument

"----------------------------------------------------------------------------------------------------------------"
"---default argument---"

def welcome(name="Guest"):      #default value is guest
    print(f"Hello , {name}!")

welcome()               #uses default value "Guest"
welcome("poojan")       #uses Poojan

# End of Program
# Thank You
# Program Finished


