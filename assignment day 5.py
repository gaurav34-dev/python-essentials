#!/usr/bin/env python
# coding: utf-8

# # QUESTION 2

# In[16]:



#for num in range(1,2500):
def checkPrime(num):
    if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
            return False
            break
       else:
         return True
         #print(num)
            
            
            
            
            
            
            
checkPrime(7)


# In[17]:


lst = list(range(2500))


# In[18]:


lst_prime = []


# In[19]:


for item in lst:
    if checkPrime(item):
        lst_prime.append(item)


# In[21]:


print(lst_prime)


# In[22]:



lst_prime_one = filter(checkPrime,lst)


# In[23]:


print(list(lst_prime_one))


# QUESTION3 

# In[1]:


def Capitalize(string):
     return string.title()
    #return string.capitalize()

Capitalize("ramesh")


# In[2]:


lst1 = ["hey this is sai","i am from mumbai","letsupgrad","python batch 7","interesting","fantastic"]


# In[3]:



lst_new = map(lambda string: string.title(), lst1)


# In[4]:



list(lst_new)


# # question 1

# In[2]:


lst=['1','1','5']


# In[3]:



lst1=[]
num=""
while (num)!=" ":
    num=input("enter the numbers to be in a list and press space to end the list:" )
    lst1.append(num)


# In[4]:


lst1


# In[5]:


lst1.pop()


# In[6]:


lst1


# In[38]:


lst2=[]
lst2=lst1.index(lst[0:])
if(lst2.len()!=0):
  try:
      print("its a match")
  except exception as e:
      print(e)


# In[22]:


j=lst1.index(lst[0])
j


# In[14]:


z=lst1[j+1:].index(lst[1])


# In[15]:


z


# In[20]:


k=lst1[z+1:].index(lst[2])
print(k)


# In[ ]:




