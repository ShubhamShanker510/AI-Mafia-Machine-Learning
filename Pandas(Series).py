#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install pandas


# In[4]:


pip install numpy


# In[5]:


import numpy as np
import pandas as pd


# # Creating a series
# ### You can convert a list,numpy array or dictionary to a series

# In[10]:


# labels array
labels=['a','b','c']

#list array
my_list=[10,20,30]

arr=np.array([10,20,30])

#dictionary
d={'a':10,'b':20,'c':30}
a=pd.Series(d)
a['a']
a['c']


# #####  ** Using Lists **

# In[11]:


pd.Series(data=my_list)


# In[12]:


pd.Series(index=labels,data=my_list)
#keyword argument


# In[13]:


pd.Series(labels,my_list)


# ##### ** Numpy Arrays **

# In[14]:


pd.Series(arr)


# In[15]:


pd.Series(arr,labels)


# ##### ** Dictionary **

# In[16]:


pd.Series(d)


# ### Data in Series
# #### A pandas Series can hold a variety of object types

# In[17]:


pd.Series(data=labels)


# In[18]:


# Even functions(although unlikely that you will use this)
pd.Series([sum,print,len])


# ### Using an index 
# The key to using a Series is understanding its index.Pandas makes use of these index names or number by allowing for fast look ups of information(works likes a hash tble or dictionary)

# In[19]:


ser1=pd.Series([1,2,3,4],index=['USA','Germany','USSR','Japan'])


# In[20]:


ser1


# In[21]:


ser2=pd.Series([1,2,5,4],index=['USA','Germany','Italy','Japan'])


# In[22]:


ser2


# In[23]:


ser1['USA']


# Operations are then also done based off of index

# In[24]:


ser1+ser2


# In[ ]:




