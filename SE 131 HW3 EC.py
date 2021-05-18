#!/usr/bin/env python
# coding: utf-8

# In[27]:


import numpy as np


# In[28]:


x = np.array([1/25.7568])
x


# In[29]:


gradN_ABC = x*np.array([[4.08, 1.94],[-6,3.46],[1.92,-5.4]])
print(gradN_ABC)


# In[32]:


gradN_BCA = x*np.array([[7.32, 9.46],[-5.4,-3.46],[-1.92,-6]])
print(gradN_BCA)


# In[33]:


gradN_CAB = x*np.array([[2.14, -7.32],[1.94,5.4],[-4.08,1.92]])
print(gradN_CAB)


# In[ ]:




