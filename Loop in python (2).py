#!/usr/bin/env python
# coding: utf-8

# # Loops in Python

# While Loop:

# In[1]:


i = 1
while i <= 3:
    print("Hay!")
    i = i+1


# # For Loop:
# The for statement in python differs a bit from what you may used in C. Rather than always iterating over an arithmatic progression of numbers, or giving the user the ability to define both the iteration step and halting condition, Python's for statement iterates over the items of any sequence(a list or a string), in the order that they appear in the sequence. 
# 

# # List
# Python knows a number of compound data types, and support the common operations supported by such types.
# 
# 

# In[2]:


# list
for i in [0,1,2]: #----> For list we use square brackets.
    print("Hay")


# # The range() Function:
# If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy. It generates arithmetic progressions.
# To iterate over the indices of a sequence, you can combine range() and len() as follows.
#  

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


# # Break and Continue Statements, and else Clauses on Loops

# The break statement, like in C, breaks out of the innermost enclosing for or while loop.
# 
# Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the list (with for) or when the condition becomes false (with while), but not when the loop is terminated by a break statement. 

# # Pass Statements
# The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action.

# In[6]:


while True:
    n= int(input("What's n?"))
    if n>0:
        break
        
for _ in range(n):
    print("Hay")


# # Functions
# The keyword def introduces a function definition. It must be followed by the function name and the parenthesized list of formal parameters. The statements that form the body of the function start at the next
# line, and must be indented.
# 
# The first statement of the function body can optionally be a string literal; this string literal is the function’s documentation string, or docstring. (More about docstrings can be found in the section Documentation. More Control Flow Tools Strings.) There are tools which use docstrings to automatically produce online or printed documentation,
# or to let the user interactively browse through code; it’s good practice to include docstrings in code that you write, so make a habit of it.
# 
# A function definition introduces the function name in the current symbol table. The value of the function
# name has a type that is recognized by the interpreter as a user-defined function. This value can be assigned
# to another name which can then also be used as a function.

# In[7]:


while True:
    n = int(input("What's n?"))
    if n>0:
        break
        
def Hay()
    for _ in range(n):
    print("Hay")


# In[8]:


def main():
    Hay(3)
    
def Hay(n):
    for _ in range(n):
        print("hay")
        
main()


# The return statement returns with a value from a function. return without an expression argument returns None. Falling off the end of a function also returns None.
# 
# 
# The statement result.append(a) calls a method of the list object result. A method is a function that ‘belongs’ to an object and is named  obj.methodname, where obj is some object (this may be an expression), and methodname is the name of a method that is defined by the object’s type. Different types define different methods.   

# In[1]:


def main():
    number = get_number()
    Hay(number)
    
def get_number():
    while True:
        n = int(input("What's n?"))
        if n>0:
            break
    return n
    
    
def Hay(n):
    for _ in range(n):
        print("Hay")
        
        
main()
        
        
        
        


# # List
# 

# In[11]:


students = ["hermione","Harry","Ron"]
print(students)


# In[12]:


students = ["Hermione","Harry","Ron"]
print(students[0])
print(students[1])
print(students[2])


# In[13]:


students = ["Hermione","Harry","Ron"]
for student in students:
    print(student)


# In[16]:


students = ["Hermione","Harry","Ron"]
for i in range(len(students)):
    print(students[i])


# In[17]:


students = ["Hermione","Harry","Ron"]
for i in range(len(students)):
    print(i, students[i])


# In[18]:


students = ["Hermione","Harry","Ron"]
for i in range(len(students)):
    print(i+1, students[i])


# # Dictionary or dict

# In[20]:


students = {
    "Hermione":"Gryffidor",
    "Harry":"Gryffidor",
    "Ron":"Gryffidor",
    "Draco":"Slytherin",
}
print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])





# In[21]:


students = {
    "Hermione":"Gryffidor",
    "Harry":"Gryffidor",
    "Ron":"Gryffidor",
    "Draco":"Slytherin",
}

for student in students:
    print(student)


# In[24]:


students = {
    "Hermione":"Gryffidor",
    "Harry":"Gryffidor",
    "Ron":"Gryffidor",
    "Draco":"Slytherin",
}

for student in students:
    print(student, students[student], sep=": ")


# In[29]:


# for having lots of lists in dictionary
students = [
    {"Name":"Hermione", "house":"Gryffidor", "Patronus":"Otter"},
     {"Name":"Harry", "house":"Gryffidor", "Patronus":"Stag"},
     {"Name":"Ron", "house":"Gryffidor", "Patronus":"Jack Russell Terrier"},
     {"Name":"Draco", "house":"Slytherin", "Patronus":None}
]
for student in students:
    print(student["Name"], student["house"], student[ "Patronus"], sep= ": ")



# In[37]:


def main():
    print_column(3)
        
def print_column(height):
    for _ in range(height):
        print("#\n" * height, end="")
        
main()


# In[38]:


def main():
    print_row(4)
    
def print_row(width):
    print("?" * width)
    
    
main()


# In[44]:


def main():
    print_square(3)
        
def print_square(size):
    
    #For each row in square
    for i in range(size):
        
        #For each brick in row
        for j in range(size):
            
            #print brick
            print("#",end="")
            
        print()
        
        
main()


# In[45]:


def main():
    print_square(3)
        
def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)
    
main()

        
    


# In[ ]:




