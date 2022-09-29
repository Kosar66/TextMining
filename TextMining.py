#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv('per.csv')


# In[3]:


data.head()


# In[4]:


with open('stopwords.txt') as stopwords_file :
    stopwords = stopwords_file.readlines()
stopwords = [line.replace('\n' , '') for line in stopwords]
stopwords


# In[5]:


pip install nltk


# In[6]:


import nltk


# In[7]:


nltk.download('stopwords')
nltk.download('punkt')


# In[8]:


nltk.stopwords =  nltk.corpus.stopwords.words('english')
stopwords.extend(nltk.stopwords)
len(stopwords)


# In[9]:


pip install hazm


# In[10]:


import hazm


# In[ ]:




