#!/usr/bin/env python
# coding: utf-8

# # Question2

# In[4]:


try:
    file=open("letsupgrad.txt","w");
    p=file.read();
    print(p);
    file.close();
    print("success");
except Exception as e:
    print(e);


# # Question1

# In[19]:


def getInput(calculate_arg_fun):
    def wrap_function():
        print("Hey people enter number =")
        a = int(input("Enter your first Number - "))
        #b = int(input("Enter your second Number - "))
        calculate_arg_fun(a)   
    return wrap_function


# In[20]:


@getInput
def checkoddeven(num1):
    if(num1%2==0):
        print("the number " +str(num1)+" is even")
    else:
        print("the number "+str(num1)+" is odd")
    


# In[21]:


checkoddeven()


# In[22]:


checkoddeven()


# In[ ]:




