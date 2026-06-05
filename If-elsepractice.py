print("===================================")
print("   Welcome to Python Practice File ")
print("   Let's learn, build, and improve ")
print("===================================")

"""Author - Poojan"""
# Here i am going to practice if-else questions normal to advance.

"------------------------------------------------------------------------------------------------------------"

# date(05/06/2026)

""" 1. Even or Odd

 Write a program that takes a number as input and checks whether it is even or odd."""
"------------------------------------------------------------------------------------------------------------"

num1 = int(input("Provide Your first number - "))


if num1%2==0 :
    print(f"{num1} is even")
else:
    print(f"{num1} is odd")

"------------------------------------------------------------------------------------------------------------"
"""2-Positive, Negative, or Zero

Write a program that takes a number and prints:

“Positive” if number > 0
“Negative” if number < 0
“Zero” if number == 0"""
"------------------------------------------------------------------------------------------------------------"

num2 = int(input("Provide your number - "))

if num2==0:
    print(f"{num2} is zero")

elif num2>0:
    print(f"{num2} is positive")

elif num2<0:
    print(f"{num2} is negative")

"------------------------------------------------------------------------------------------------------------"

"""3. Voting Eligibility

Write a program that takes age as input and checks:

If age ≥ 18 → “Eligible to vote”
Else → “Not eligible to vote”"""

"------------------------------------------------------------------------------------------------------------"

age = int(input("Provide your age - "))

if age >= 18:
    print("You are eligible for Voting")
else:
    print("You are not eligible")

"------------------------------------------------------------------------------------------------------------"
"""4. Largest of Two Numbers

Take two numbers as input and print which one is greater, or if both are equal."""
"------------------------------------------------------------------------------------------------------------"

a1 = int(input("Provide first number -  "))
a2 = int(input("Provide second number -  "))

if a1>a2:
    print(f"{a1} is greater than {a2}")
elif a2>a1:
    print(f"{a2} is greater than {a1}")
elif a1==a2:
    print(f"{a1} {a2} both are equal")
    
"------------------------------------------------------------------------------------------------------------"
"""5. Pass or Fail

A student’s marks are given as input.

If marks ≥ 40 → “Pass”
Else → “Fail”"""

a3 = int(input("Provide your obtained marks - "))

if a3 >= 40:
    print("You passed the test")
else:
    print("better luck next time")

"------------------------------------------------------------------------------------------------------------"





print("===================================")
print("   Thank you for practicing today  ")
print("   Keep coding, keep growing 🚀     ")
print("   See you in the next session!     ")
print("===================================")
