#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Ask user for their name
'''for paragraph'''
name = input("What's your name?")

#Say hello to user
print("hello,", name)


# In[2]:


#print(*objects, sep='','\n',file=sys.stdout, flush=False)-----> documentation and format of print statement.
#Ask user for their name
'''for paragraph'''
name = input("What's your name?")

#Say hello to user
print("hello, ", end="")
print(name)


# In[3]:


name = input("What's your name?")#method2
print("hello,", name, sep='!!!!')




# In[4]:


#say hello to user
print("hello, \"friend\"")


# In[5]:


#Ask user for their name
name=input("What's your name?")

#Say hello to user
print(f"hello, {name}")
# treats like special string and 3 method of print statement.


# In[6]:


#Ask user for their name
name=input("What's your name?")

#remove whitespace from str
name=name.strip()

#capitalize user's name
name=name.capitalize()

#Say hello to user
print(f"hello, {name}")


# In[7]:


#Ask user for their name
name=input("What's your name?").strip().title()

#Say hello to user
print(f"hello, {name}")


# In[8]:


#Ask user for their name
name=input("What's your name?").strip().title()

#split user's name into first name and last name
first, last = name.split(" ")

#Say hello to user
print(f"hello, {first}")



# In[9]:


#calculation
x = input ("What's x? ")
y = input ("What's y? ")
z = x + y
print(z)
#treats like character, simply writes the value.


# In[10]:


#calculation
x = input ("What's x? ")
y = input ("What's y? ")
z = int(x) + int(y)
print(z)


# In[11]:


#calculation
x = int(input ("What's x? "))
y = int(input ("What's y? "))
print(x+y)


# In[2]:


#round(number[, ndigits])------>documentation ,used to round float data to nearset integer.
#calculation
x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x + y)

print(f"{z:,}")#--->can used to give from what place of digit we want to round off.


# In[3]:


def hello(): #---> now all the below codes were recognized from def function.
    print("hello")
    
name= input("what's your name?")
hello()
print(name)


# In[4]:


def hello(to): #---> now all the below codes were recognized from def function.
    print("hello,", to)
    
name= input("what's your name?")
hello(name)


# In[ ]:


def hello(to="world"): #---> now all the below codes were recognized from def function.
    print("hello,", to)
    
hello()
name= input("what's your name?")
hello(name)


# In[ ]:




