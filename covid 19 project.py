#!/usr/bin/env python
# coding: utf-8

# # DATA ANALYSIS OF COVID-19 CASES IN ITALY

# In[ ]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl


# In[18]:


x = pd.read_csv("C:\\Users\\vigne\\Downloads\\archive\\covid19_italy_region.csv")


# In[19]:


x


# In[20]:


x.head()


# In[21]:


x.tail()


# In[22]:


x.describe()


# In[24]:


x.columns


# # RELATING VARIABLES WITH SCATTER PLOTS

# In[28]:


sns.pairplot(x)


# In[29]:


sns.relplot(x='Recovered',y='Deaths',data=x)


# In[30]:


sns.relplot(x='Recovered',y='Deaths',kind='line',data=x) 


# In[31]:


x.describe()


# In[32]:


x.columns


# In[33]:


sns.relplot(x='Country',y='Deaths',kind = 'line',data = x)


# In[34]:


sns.catplot(x='Country',y='Deaths',data = x)


# In[ ]:




