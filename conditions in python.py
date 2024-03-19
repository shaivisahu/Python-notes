#!/usr/bin/env python
# coding: utf-8

# # conditions in python

# use to compare things <,>,<=,>=,==,!=
# 

# In[3]:


x = int(input("What's x?"))
y = int(input("Wat's y?"))

if x<y:
    print("x is less than y")
if x>y:
    print("x is greater than y")
elif x ==y:
    print("x is equal to y")
    


# In[5]:


# use of elif give systematic  structure to our codes.
x = int(input("What's x?"))
y = int(input("Wat's y?"))

if x<y:
    print("x is less than y")
elif x>y:
    print("x is greater than y")
elif x ==y:
    print("x is equal to y")


# In[9]:


x = int(input("What's x?"))
y = int(input("What's y?"))

if x<y or x>y:
    print("x is not equal to y")
else:
    print("x is equal to y")


# In[8]:


# more simple than privious
x = int(input("What's x?"))
y = int(input("What's y?"))

if x== y:
    print("x is not equal to y")
else:
    print("x is equal to y")




# In[3]:


#codes for checking scores
score = int(input("Score:"))
if score <= 100 and score >90:
    print("You passed with grade A")
elif score <= 90 and score >80:
    print("you passed with grade B ")
elif score <= 80 and score >70:
    print("You passed with grade c ")
elif score <= 70 and score >60:
    print("you passed with gradw D")
else:
    print ("You are fail")
    


# In[4]:


def main():
    x = int(input("What's x?"))
    if is_even(x):
        print("Even")
    else:
        print("odd")
        
        
def is_even(n):
    if n % 2== 0:
        return True
    else:
        return False
    
main()


# In[5]:


def main():
    x = int(input("What's x?"))
    if is_even(x):
        print("Even")
    else:
        print("odd")
        
        
def is_even(n):
    return True if n % 2== 0 else False


main()


# In[6]:


name = input("What's your name? ")

if name=="harry":
    print("Gryffindor")
elif name=="Hermione":
    print("Gryffindor")
elif name=="Ron":
    print("gryffindor")
elif name=="Draco":
    print("Slytherin")
else:
    print("Who?")


# In[8]:


name = input("What's your name? ")

match name:
    case "harry":
        print("Gryffindor")
    case "Harmione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
        


# In[ ]:




