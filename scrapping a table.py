#!/usr/bin/env python
# coding: utf-8

# In[8]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

# getting the html

url = "http://tsenomer.ru/goroda/moscow/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "lxml") 
soup


# In[9]:


# getting the table

table = soup.find('table', {'class': "price_tab"})
# table


# In[44]:


data = []
 
for i in table.find_all('td'):
    row = i.text 
    data.append(row)
    
# data


# In[45]:


headers =[]

for i in range(4):
    headers.append(data[i])
    
# headers


# In[101]:


df = pd.DataFrame(columns = headers)
# df


# In[102]:


data = data[4:]
# data


# In[103]:


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield data[i:i + n]


# In[84]:


# import pprint
# pprint.pprint(list(chunks(data, 4)))


# In[115]:


# df


# In[117]:


for row in (list(chunks(data, 4))):
    df.loc[len(df)] = row


df

