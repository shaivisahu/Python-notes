#!/usr/bin/env python
# coding: utf-8

# # Loops in Python

# While Loop:

# In[1]:


i = 1
while i <= 3:
    print("Hay!")
    i = i+1


# For Loop:
# 

# In[2]:


# list
for i in [0,1,2]: #----> For list we use square brackets.
    print("Hay")


# In[3]:


for i in range(7):
    print("Hay")


# In[4]:


for _ in range(7):
    print("Hay")


# In[5]:


print("Hay\n"*3) # \n--> is used for escape sequence.


# In[6]:


print("Hay\n"*3, end="") 


# In[7]:


while True:
    n = int(input("What's n?"))
    if n>0:
        break
        
for _ in range(n):
    print("Hay")


# In[ ]:




