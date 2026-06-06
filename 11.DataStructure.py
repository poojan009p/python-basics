"""
Topic: Data Structure 
Author: Poojan
Description: Basic examples of Data Structure.
""" 

"----------------------------------------------------------------------------------------------------------------"
"---Data Structure---"
# data structures are different ways to organize and store data in Python so that you can use it efficiently.

"there are total four data structures"

# - list
# - tuple
# - set
# - dict

"---LIST---"

# A list stores multiple items in order.

Fruits = ["apple","mango","banana"]   # When to use?

                                      # When you have a collection of items and order matters

"---TUPLE---"

# A tuple is like a list, but it cannot be changed.

colors = ("red", "green", "blue")    # When to use?

                                     # When data should stay fixed.

"---DICTIONARY---"

# Stores data as key : value pairs.

student = {
    "name": "Poojan",               # When to use?
    "age": 23,                      # When every value has a label.
    "city": "Veraval"
}

"---SET---"

# Stores unique values only.

# numbers = {1, 2, 3, 4}
numbers = {1, 1, 2, 2, 2, 3, 4, 4}

number = set(numbers)      # Finding unique values.

print(number)

# | Data Structure | Ordered | Changeable | Duplicates          |
# | -------------- | ------- | ---------- | ------------------- |
# | List           | ✅       | ✅          | ✅                   |  -> most imp for data science
# | Tuple          | ✅       | ❌          | ✅                   |
# | Dictionary     | ✅       | ✅          | Keys must be unique |    -> most imp for data science
# | Set            | ❌       | ✅          | ❌                   |
