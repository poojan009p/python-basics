"""
Topic: String indexing and Slicing
Author: Poojan
Description: Basic examples of Python String indexing and Slicing.

"""
"--------------------------------------------------------------"
"---String Indexing---"

name = "poojan"

print(name[0])  #p
print(name[1])  #o
print(name[2])  #o      # Positive indexing starts from 0 
print(name[-3]) #j      # Negative indexing starts from -1
print(name[-2]) #a  
print(name[-1]) #n

"--------------------------------------------------------------"
"---String Slicing---"

text = "PoojanThummer"

print(len(text))    #gives length of string 
print(text[0:6])    #Poojan
print(text[6:13])   #Thummer
print(text[:6])     #Poojan
print(text[6:])     #Thummer
print(text[::-1])   #remmuhTnajooP

print(text.upper())  # Make Uppercase everything
print(text.lower())  # Make Lowercase everything
print(text.capitalize()) # Capitalize everything
print(text.replace("PoojanThummer","Poojan"))  # replace PoojanThummer -> Poojan

# End of Program
# Thank You
# Program Finished
