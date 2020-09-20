#!/usr/bin/env python
# coding: utf-8

# # Question1

# In[34]:


get_ipython().run_cell_magic('writefile', 'simple_code.py', "'''this is a code'''\ndef check_prime(num):\n    '''prime or not'''\n    if num > 1:\n        for i in range(2, num):\n            if (num % i) == 0:\n                return False\n                break\n            else:\n                return True       ")


# In[35]:


import simple_code
simple_code.check_prime(7)


# In[36]:



get_ipython().system(' pip install pylint')


# In[37]:


get_ipython().system(' pylint "simple_code.py"')


# In[38]:


get_ipython().run_cell_magic('writefile', 'testCap.py', '\nimport unittest\nimport simple_code\n\nclass testDigit(unittest.TestCase):\n    def testSingleDigit(self):\n        abc = 5\n        result = simple_code.check_prime(abc)\n        self.assertEqual(result, True)\n        \n    def testingTwoDigit(self):\n        xyz = 23\n        result = simple_code.check_prime(xyz)\n        self.assertEqual(result,True)\n\nif __name__ == "__main__":\n    unittest.main()')


# In[39]:


get_ipython().system(' python testCap.py')


# # Question2

# In[40]:


#import numpy as np
def getarmstrongnumber(lst):
      for n in lst:
        global s;
        global m;
        s=0;
        m=n;
        while(n!=0):
            r=n%10;
            s=(s+(r**3));
            n=n//10;
        if(m==s):
            yield m;
    #else:
        #yield False;


# In[41]:


lst = list(range(1000))


# In[42]:


lst


# In[43]:


print(list(getarmstrongnumber(lst)))


# In[ ]:




