#!/usr/bin/env python
# coding: utf-8

# QUESTION1         

# In[1]:


class Bankaccount():
    def __init__(self,Ownername,Balance,add,withdraw):
        self.Ownername=Ownername;
        self.Balance=Balance;
        self.add=add;
        self.withdraw=withdraw;
        
    def Deposit(self):
        #self.add=add;
        self.Balance=self.Balance + self.add;
        print("the addition is "+ str(self.add));
        print("the new balance after addition is "+ str(self.Balance));
        
    def Withdraw(self):
        #self.withdraw=withdraw;
        if(self.withdraw>self.Balance):
            print("this withdraw is invalid");
        else:
            print("the withdraw is "+str(self.withdraw));
            self.Balance=self.Balance-self.withdraw;
            print("the new balance after withdrawal is "+str(self.Balance));
            


# In[2]:


b1=Bankaccount("ramesh",700,800,1600);


# In[3]:


b1.Balance


# In[4]:


b1.withdraw


# In[5]:


b1.Withdraw()


# In[6]:


b1.Deposit()


# In[7]:


b1.Withdraw()


# In[8]:


b1.Ownername


# In[9]:


b1=Bankaccount("ramesh",700,800,500);


# In[10]:


b1.Ownername


# In[11]:


b1.add


# In[12]:


b1.withdraw


# In[13]:


b1.Balance


# In[14]:


b1.Deposit()


# In[15]:


b1.Withdraw()


# Question2 

# In[18]:


import math as m
class Cone():
    def __init__(self,Radius,Height):
        self.Radius=Radius;
        self.Height=Height;
    
    def Volume(self):
        volume=(1/3)*(m.pi)*(self.Radius**2)*(self.Height);
        print("the volume of cone is "+ str(volume));
        
    def SurfaceArea(self):
        length=m.sqrt(self.Radius**2 + self.Height**2);
        surfacearea=(m.pi)*(self.Radius)*(self.Radius + length);
        print("the surfacearea is "+ str(surfacearea));
    


# In[19]:


b1=Cone(3,4);


# In[20]:


b1.SurfaceArea()


# In[21]:


b1.Volume()


# In[ ]:




