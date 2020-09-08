#!/usr/bin/env python
# coding: utf-8

# In[1]:


list=['ram',1,'rinki','sa@gmail.com','rumi','sushant'];


# In[2]:


list.append("sunil")


# In[3]:


list


# In[8]:


list.sort()


# In[14]:


list1=['abhishekh','raj','jignesh'];
list1.sort();
list1


# In[17]:


list2=list1.copy();
list2


# In[21]:


list2.count('abhishekh');


# In[22]:


list2.count('abhishekh')


# In[24]:


list2.extend(list);


# In[25]:


list2


# # dictionary and default functions

# In[26]:


dict={"name":"ramesh turoe","address":"1011 shanti nagar","email":"tingu@gmail.com","mobile number":9564321211};


# In[27]:


get_ipython().run_line_magic('pinfo', 'dict.get')


# In[28]:


dict.get("name")


# In[29]:


get_ipython().run_line_magic('pinfo', 'dict.update')


# In[32]:


dict.update({"bill":2345})


# In[33]:


dict


# In[36]:


dict.update({"name":"shivi"})


# In[37]:


dict


# In[43]:


get_ipython().run_line_magic('pinfo', 'dict.fromkeys')


# In[42]:


vowels = dict.fromkeys()
print(vowels)


# In[45]:


dict.popitem()


# In[46]:


dict


# In[47]:


get_ipython().run_line_magic('pinfo', 'dict.update')


# In[50]:


dict.update({'bill':234556})


# In[51]:


dict


# In[53]:


dict.clear()


# In[54]:


dict


# In[55]:


# sets and its default functions


# In[4]:


set={1,2,2,4,33,50}


# In[57]:


set


# In[8]:


set1={3,5,7,8,9,13,33,50}


# In[61]:


print(set.intersection(set1));


# In[62]:


print(set.union(set1))


# In[63]:


get_ipython().run_line_magic('pinfo', 'set.pop')


# In[6]:


print(set.pop());


# In[2]:


set.pop(5)


# In[3]:





# In[11]:


print(set1.difference(set));


# In[12]:


set1.issubset({3,5,7,8,9,13,15,17,19})


# In[17]:


tuple=(6,8,9,10,13,8,17,21);


# In[14]:


get_ipython().run_line_magic('pinfo', 'tuple.count')


# In[18]:


print(tuple.count(8));


# In[20]:


print(tuple.index(8));


# In[21]:


String="austrailia"


# In[23]:


print(String.startswith("a"));


# In[24]:


print(String.count("a"));


# In[25]:


print(String.upper());


# In[27]:


String.find("a")


# In[30]:


String.find("u")


# In[32]:


print(String.endswith("a"));


# In[ ]:




