#!/usr/bin/env python
# coding: utf-8

# # armstrong number

# In[ ]:


for n in range(1042000,702648265):
    s=0;
    m=n;
    while(n!=0):
        r=n%10;
        s=(s+(r**3));
        n=n//10;
    if(m==s):
        print(m);
        break;


# In[ ]:




