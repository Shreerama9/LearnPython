#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


my_math = [[1,2,3],[4,5,6],[7,8,9]]


# In[4]:


np.array(my_math)


# In[6]:


np.arange(0,21,2)


# In[8]:


np.zeros(3)


# In[9]:


np.ones(8)


# In[11]:


np.zeros((2,3))


# In[14]:


np.ones((4,3))


# In[15]:


np.linspace(0,5,10)


# # *np.lindspace 3 num will decide number of points 1 and 2*

# In[17]:


np.random.rand(5,5)


# *np.random has many features*

# In[18]:


np.eye(4,3)


# In[19]:


np.random.power(2,4)


# In[20]:


np.random.randn(2)


# In[21]:


np.random.randint(1,100,20)


# In[22]:


arr = np.arange(25)


# In[23]:


arr


# In[24]:


arr.reshape(5,5)


# #no. of elements = (a,b)

# In[25]:


arr.max()


# In[26]:


arr.min()


# In[31]:


#locarion arg


# In[29]:


arr.argmax()


# In[30]:


arr.argmin()


# In[32]:


arr.shape


# In[33]:


arr.reshape(5,5)


# In[38]:


#datatype 
arr.dtype


# In[39]:


from numpy.random import randint


# In[40]:


randint(5,10)


# In[9]:


import numpy as np


# In[10]:


arr = np.arange(0,11)


# In[11]:


arr


# #slicing index

# In[12]:


arr[4:]


# In[13]:


arr[0:8] = 100


# In[14]:


arr


# In[19]:


slice_of_arr = arr[:5]


# In[20]:


slice_of_arr


# In[21]:


slice_of_arr[:3] = 75


# In[22]:


slice_of_arr


# In[23]:


arr


# In[25]:


arr_copy = arr.copy()
arr_copy


# In[ ]:




