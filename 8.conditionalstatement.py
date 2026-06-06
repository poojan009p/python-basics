"""
Topic: Conditional Statement 
Author: Poojan
Description: Basic examples of Conditional Statement.
"""

"--------------------------------------------------------------------------------------------"
"---Conditional Statement---"
# It allow to make decision by executing different blocks of codes based on condition

"-------Types of Condition Statements------"

"   If              - executes if the condition is True. "
"   If-else         - executes if True another is False."
"   If-elif-else    - checks multiple conditions in sequence."  

"------If condition----"

x = 9

if x == 9:              # checks the condition
    print("True")

"--------------------------------------------------------------------------------------------"
"------If-else condition----"

a = 9

if a == 10:              # checks the condition if true then execute or else will execute
    print("True")

else: 
    print("False")

"--------------------------------------------------------------------------------------------"
"------If-elif-else condition----"  
   
num = int(input("Provide any number"))

if num > 0:
    print("Given number is greater than zero")

elif num == 0:
    print("Given number is zero")

else :
    print("Given number is less than zer")


# End of Program
# Thank You
# Program Finished
