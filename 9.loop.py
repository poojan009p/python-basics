"""
Topic: Loops 
Author: Poojan
Description: Basic examples of Loops.
"""
"---Loops---"
# Loops - Loops in python allow us to execute block of code multiple times without rewriting it.

"""---Types of loops---"""
    # for loop 
    # while loop

"---For loop---"

#  range() - it is used to generate a sequence of numbers , which is commonly used in loops.

# for numbers

for i in range(10):
    print(i)

# for string

p = "poojan"

for i in range(len(p)):
    print(i)

# other method - this method gives direct access to characters instead of index values

for char in p:
    print(char)

"---While loop---"

#  it repeats the loop as long as condition is True. It is useful when the number of iteration is unknown.

# while p:
    # code to execute

count =0 

while count<=9:
    print(f"Total count {count}")
    count += 1

