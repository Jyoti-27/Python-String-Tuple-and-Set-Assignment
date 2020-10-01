#!/usr/bin/env python
# coding: utf-8

# - Q.1 Define different types of variables (integer, boolean, string, float, complex) and print their values and their types.

# In[44]:


a = 1 # Integer data type
print(a) # Print value
print(type(a))  # Print the data type


# In[45]:


b = True # Boolean data type
print(b) # Print value
print(type(b))  # Print the data type


# In[46]:


c = "Success" # String data type
print(c)  # Print value
print(type(c))  # Print the data type


# In[47]:


d = 9.5 # Float data type
print(d)  # Print value
print(type(d))   # Print the data type


# In[48]:


e = 3 + 6j # Complex data type
print(e)   # Print value  
print(type(e))   # Print the data type


# - Q.2 In the above question convert float variable into integer type and integer variable into str type.

# In[34]:


d = 9.5 # Float data type
print(d)    # Print value
print(type(d))  # Print the data type
f = int(d)   # Conversion of float into integer
print(f)    # Print value
print(type(f))    # Print the data type


# - Q.3 What will you get converting “abc” into boolean ? 

# In[37]:


h = "abc" # String data type
print(h)   # Print value
print(type(h))  # Print data type
i = bool(h)  # Conversion of string data type into boolean data type
print(i)    # Print value
print(type(i))  # Print data type


# -  Q.4 Print the substring from index 2 to index 4 for any given string. For example (llo) from “Hello World” 

# In[40]:


k = "Jyoti Sabarad" # Defining  a string data type
print(k)    # Print value
l = (k[2 : 5]) # substring from index 2 to index 4
print(l)  # Print value


# - Q.5 Write a program to check a substring in a given string. For example 'e' is present in the word 'Umbrella' 

# In[47]:


String =  'Umbrella'   # Defining given string data type
print(String)  # Print string
sub_str = 'e'  # sustring
if(String.find(sub_str) == -1):  # Check is substring is present or not.
     print("Substring is not found in String!")  # Print substring is not found
else:
     print("Substring is present in String!")   # Print substring is found


# - Q.6 Use the correct comparison operator to check if 5 is not equal to 10. 

# In[49]:


w = 5 # First string
u =10 # Second string
print(w != u)  # Print 5 is not equal to 10 is true 


# - Q.7 Write a program to get a string from the user and sort the words of the string in alphabetical order. 

# In[50]:


my_str = input("Jyoti")  # Define an input string
words = my_str. split() # Breakdown the string into a list of words.
words.sort() # sort the list.
print(words) # Print the sorted words.


# - Q.8 . Join two words using special characters like ‘ – ‘ ,’#’ 

# In[8]:


r = input("Enter a word: ")   # First word
z = input("Enter another word: ")  # Second word
q = r + z   # Concatenation operation
print("Concatenation of two words is : " , q)  # Concate two words
v = ['J' 'y' 'o' 't' 'i''-''Y' 'o' 'g' 'e' 's' 'h']  
'-'.join(v)   # Joining of two words 


# In[9]:


t = input("Enter a word: ")   # First word
p = input("Enter another word: ")  # Second word
m = t + p
print("Concatenation of two words is : " , m)  # Concate two words
v = ['J' 'y' 'o' 't' 'i''#''Y' 'o' 'g' 'e' 's' 'h']  
'-'.join(v)   # Joining of two words 


# - Q.9 Find all occurrences of “INDIA” in a given string ignoring the case. 
#       input_str = "Welcome to INDIA. india is awesome.
# 

# In[23]:


# Case 1
input_str = "Welcome to INDIA. india is awesome."   # Define a given string 
print(input_str.count("INDIA"))      # Print the occurance of "INDIA" 


# In[22]:


# Case 2
input_str = "Welcome to INDIA. india is awesome."      # Define a given string 
M = input_str.count("INDIA") + input_str.count("india")  # The occurance of "INDIA" 
print(M)      # Print the occurance of "INDIA" and "india"


# - Q.10 Replace first two ‘l’ with ‘n’ in ‘Hello World’ 

# In[18]:


oldstring1 = 'Hello World'  # Define a given string
newstring1 = oldstring1.replace(oldstring1[2:4], 'n')  # Applying replace method for first two l insert n
print(newstring1)   # Print new resultant string


# - Q.11 Write a program that takes your full name as input and displays the abbreviations of the first and middle names except the last name which is displayed as it is. For example, if your name is Robert Brett Roser, then the output should be R.B.Roser

# In[27]:


string2 = "Jyoti Vijay Sabarad"  # Define a string
string2 = string2.split()    # Use split method
newstring2 = (string2[0][0] + '.' + string2[1][0] + '.' + string2[2])  # By taking abbreviations
print(newstring2)  # Print new resultant string


# - Q.12  Write a program to check if a given string is a Palindrome. 
#        A palindrome reads the same from front and back e.g.- aba, ccaacc, mom, etc.
# 

# In[24]:


my_str = 'Mom'    # Program to check if a string is palindrome or not and define a string
my_str = my_str.casefold()   # Make it suitable for caseless comparison
rev_str = reversed(my_str)  # Reverse the string
if list(my_str) == list(rev_str):   # Check if the string is equal to its reverse
   print("The string is a palindrome.")  # Print the string is palindrome
else:
   print("The string is not a palindrome.")  # Print the string is palindrome


# In[ ]:




