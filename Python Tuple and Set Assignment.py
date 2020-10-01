#!/usr/bin/env python
# coding: utf-8

# - Q.1 Write a Python program to add an item in a tuple. 

# In[1]:


tuple1=()    # Define an empty tuple
print(tuple1) # Print value
a=10,20,30,40   # Adding values
tuple1=a   # Adding values in empty touple
print(tuple1)  # Print tuple


# - Q.2 Write a Python program to reverse a tuple. 

# In[7]:


# First Method
x = ("Gauri")   # Define a tuple
y = reversed(x)     # Reversed the tuple
print(tuple(y))     # Reversed the tuple


# In[2]:


# Second Method
my_tuple = (1,2,3.78, 9.56,"StudyTonight")      # Define a tuple         
my_tuple = tuple(reversed(my_tuple))            # Reversed the tuple
print(my_tuple)                                 # Reversed the tuple


# - Q.3 Swap the following two tuples 
#       tuple1 = (11, 22) 
#       tuple2 = (99, 88) 
# 

# In[3]:


tuple1 = (11, 22)  # Define touple1
tuple2 = (99, 88)  # Define touple2 
tuple1, tuple2 = tuple2, tuple1  # Swapping of two touples
print(tuple1)      # Print touple1
print(tuple2)     # Print touple2


# - Q.4 . Modify the first item (22) of a list inside a following tuple to 222 
#         tuple1 = (11, [22, 33], 44, 55) 	
# 

# In[4]:


tuple1 = (11, [22, 33], 44, 55)    # Define touple1 
tuple1[1][0] = 222   # Replace the value of first position zero element with new element
print(tuple1)  # Print the new touple


# - Q.5 Write a Python program to unpack a tuple in several variables 

# In[3]:


# First Method
tuplex = 4, 8, 3   # Define a tuple
print(tuplex)   # Print vlaue
n1, n2, n3 = tuplex
print(n1 + n2 + n3)     # unpack a tuple in variables
n1, n2, n3, n4= tuplex  # The number of variables must be equal to the number of items of the tuple 


# In[5]:


# Second Method
# Python code to study about unpacking python tuple using function 

def result(x, y):  # Function takes normal arguments and multiply them 
	return x * y 
print (result(10, 100))    # function with normal variables    
z = (10, 100)      # A tuple is created  
print (result(*z))    # Tuple is passed function unpacked them 


# In[6]:


# Third Method
# Python3 program to unpack 
# tuple of lists 
from functools import reduce
import operator 
def unpackTuple(tup): 
	
	return (reduce(operator.add, tup)) 
tup = (['a', 'apple'], ['b', 'ball'])    # Driver code 
print(unpackTuple(tup))   #Print unpack tuple value


# In[7]:


# Forth Method
authors = [('Paul', 'Resnick'), ('Brad', 'Miller'), ('Lauren', 'Murphy')]
for first_name, last_name in authors:
    print("first name:", first_name, "last name:", last_name)


# - Q.6 Write a Python program to add member(s) in an empty set. 

# In[16]:


color_set = set()      # A new empty set
color_set.add("Red")   # Add color set into empty set
print(color_set)
color_set.update(["Blue", "Green"])     # Add multiple items
print(color_set)     # Print multiple color set into empty set


# - Q.7 Write a Python program to create an intersection of sets.

# In[19]:


setx = set(["green", "blue"])   # Define a first set 
sety = set(["blue", "yellow"])  # Define a second set
setz = setx & sety    # Intersection
print(setz)    # Print Intersection result


# - Q.8 Write a Python program to create a symmetric difference in sets.

# In[8]:


setx = set(["apple", "mango"])   # Define a first set 
sety = set(["mango", "orange"]) # Define a second set
setc = setx ^ sety  # Symmetric difference
print(setc)    # Print Symmetric difference result


# - Q.9  Return a set of identical items from a given two Python set 
#        set1 = [10, 20, 30, 40, 50]
#        set2 = [30, 40, 50, 60, 70] 
# 

# In[9]:


set1 = {10, 20, 30, 40, 50}   # Define a first set 
set2 = {30, 40, 50, 60, 70}  # Define a second set
if set1.isdisjoint(set2):    # Check items are identical or not
  print("Two sets have no items in iedntical")  # Two sets have no items in identical
else:
  print("Two sets have items in identical")   # Two sets have items in identical
  print(set1.intersection(set2))   # Print an identical values


# - Q.10 Remove 10, 20, 30 elements from a following set at once 
#        set1 = {10, 20, 30, 40, 50} 
# 

# In[10]:


set1 = {10, 20, 30, 40, 50}   # Define a set
set1.difference_update({10, 20, 30})    # Remove 10,20,30 from given set
print(set1)     # Print remaing elements


# - Q.11 Access value 20 from the following tuple example = ("Pooja", [10, 20, 30], (25, 50, 15)). 

# In[11]:


tuple3 = ("Pooja", [10, 20, 30], (25, 50, 15))   # Define a tuple
print(tuple3[1] [1])      # Print result of accessing value 20


# - Q.12 Count the number of occurrences of item 50 from a tuple numbers = (50, 10, 60, 70, 50).

# In[12]:


tuple4 = (50, 10, 60, 70, 50)   # Define a tuple
print(tuple4.count(50))     # Print and Count the number of occurrences of item 50 from a given tuple


# In[ ]:




