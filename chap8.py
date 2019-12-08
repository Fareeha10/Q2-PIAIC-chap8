#!/usr/bin/env python
# coding: utf-8

# # Merge
# 
# 
# #merge,join,concatinate
# #to merge it will check column first it will merge on basis of common column 
# #first col is left col
# #by defalt inner join 

# In[12]:


import pandas as pd
df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],'data1': range(7),'d2': range(7)})


# In[28]:


df2 = pd.DataFrame({'key': ['a', 'b', 'd'],'data2': range(3),'d2':range(3)})


# In[10]:


df1


# In[6]:


df2


# In[13]:


#merge can be done on bases of index,common column
pd.merge(df1,df2)


# In[14]:


#merge is not concatination |names will appear 2 times if present in both tables
#if no common columns it will give merge error now to merge we have to tell the col name to merge
df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],'data1': range(7)})


# In[15]:


df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'],'data2': range(3)})


# In[16]:


pd.merge(df3, df4, left_on='lkey', right_on='rkey')


# In[18]:


pd.merge(df3, df4, left_on='lkey', right_on='rkey',how ='outer')


# # Join
# 

# In[19]:


left2 = pd.DataFrame([[1., 2.], [3., 4.], [5., 6.]],index=['a', 'c', 'e'],columns=['Ohio', 'Nevada'])


# In[20]:


right2 = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],index=['b', 'c', 'd', 'e'],columns=['Missouri', 'Alabama'])


# In[21]:


left2


# In[22]:


right2


# In[23]:


left2.join(right2)


# In[24]:


right2.join(left2)


# In[25]:


left2.join(right2,how = 'outer')


# In[26]:


#shft+tab= all info about a function


# In[29]:


pd.merge(df1,df2,on = 'key',suffixes=('_left','_right'))


# # concatinate
# 

# In[33]:


s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s2
s3 = pd.Series([5, 6], index=['f', 'g'])
s3


# In[32]:


pd.concat([s2,s3])


# In[35]:


import numpy as np
df1 = pd.DataFrame(np.arange(6).reshape(3, 2), index=['a', 'b', 'c'],columns=['one', 'two'])


# In[36]:


import tensorflow as tf


# In[38]:


df2=pd.DataFrame(5 + np.arange(4).reshape(2, 2), index=['a', 'c'],columns=['one', 'two'])


# In[39]:


pd.concat([df1,df2])


# In[ ]:




