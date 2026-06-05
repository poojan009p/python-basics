print("===================================")
print("   Welcome to Python Practice File ")
print("   Let's learn, build, and improve ")
print("===================================")

"""Author - Poojan"""
# Here i am going to practice if-else questions normal to advance.

"------------------------------------------------------------------------------------------------------------"

# date(05/06/2026)

# --------------------------------------------------
# Exercise 1: Check whether a number is Even or Odd
# --------------------------------------------------

num1 = int(input("Provide Your first number - "))


if num1%2==0 :
    print(f"{num1} is even")
else:
    print(f"{num1} is odd")

"------------------------------------------------------------------------------------------------------------"
# -------------------------------------------------------------------
# Exercise 2: Check whether a number is Positive or Negative or Zero
# -------------------------------------------------------------------

num2 = int(input("Provide your number - "))

if num2==0:
    print(f"{num2} is zero")

elif num2>0:
    print(f"{num2} is positive")

elif num2<0:
    print(f"{num2} is negative")

"------------------------------------------------------------------------------------------------------------"

# ---------------------------------------------------------------
# Exercise 3: Check whether person is eligible for voting or not
# ---------------------------------------------------------------

age = int(input("Provide your age - "))

if age >= 18:
    print("You are eligible for Voting")
else:
    print("You are not eligible")

"------------------------------------------------------------------------------------------------------------"
# ------------------------------------
# Exercise 4: Find the largest number
# ------------------------------------

a1 = int(input("Provide first number -  "))
a2 = int(input("Provide second number -  "))

if a1>a2:
    print(f"{a1} is greater than {a2}")
elif a2>a1:
    print(f"{a2} is greater than {a1}")
elif a1==a2:
    print(f"{a1} {a2} both are equal")
    
"------------------------------------------------------------------------------------------------------------"
# -------------------------------------------------
# Exercise 3: Check whether person is Pass or Fail
# -------------------------------------------------

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
