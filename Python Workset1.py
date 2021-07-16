#!/usr/bin/env python
# coding: utf-8

# In[27]:


print(2//3)


# In[28]:


print(6<<2)


# In[29]:


print(6&2)


# In[30]:


print(6|2)


# In[31]:


# To find Factorial numner

i=int(input(" Enter Number "))
fac=1
while i>0:
    fac=fac*i
    i=i-1
print("Factorial=",fac)


# In[17]:


# To  find whether a number is prime or composite

num = int(input("Enter a number : "))

if num > 1:
    for i in range (2, num):
        if num % i == 0:
            print (num, "is not a prime number")
            break
    else:
        print(num, "is a Prime Number")
elif num == 0 or num == 1:
    print(num, " is Neither prime nor Composite number.")
else:
    print(num, " is a prime number")


# In[18]:


# To check whether a given string is palindrome or not

def check(st):
    rev=st[::-1]
    print("String  : ",st)
    print("Reverse : ",rev)
    if(st==rev):
        return True
    else:
        return False
x=input("Enter a String : ")
if check(x):
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")


# In[23]:


# To get the third side of right-angled triangle from two given sides.

from math import sqrt
print("Enter the Lenght")

a= float(input("a : "))
b= float( input("b: "))

c= sqrt(a**2 + b**2)
print("the lenght of the third side is " , c)


# In[26]:


# To print the frequency of each of the characters present in a given

na = input("Enter any String ")
ch = input("Enter seach Character ")
f = 0
for i in na:
    if i == ch:
        f=f+1
print("Number of time Found =",f)


# In[ ]:




