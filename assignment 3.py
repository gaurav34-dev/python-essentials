#!/usr/bin/env python
# coding: utf-8

# In[2]:


#question 1

altitude=input("enter the height :")
if int(altitude)<=1000:
    print("land the plane")
elif (int(atitude)>1000 and int(altitude)<5000):
    print("come down to 1000");
elif int(altitude)>5000:
    print("go around and try again");


# # question 2
# 

# In[4]:


for num in range(1,200):
    if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


# In[ ]:




