
# coding: utf-8

# In[1]:

import sqlite3
import pandas as pd
conn = sqlite3.connect('D:\GSU\Data Programming\Python Project\Final Project - Video Games\python_omegA.sqlite')


df = pd.read_sql_query("SELECT * FROM videogames", conn)
print(df)


# In[2]:

import sqlite3
import pandas as pd
import pandas as pd
get_ipython().magic(u'matplotlib inline')
from matplotlib.pyplot import hist
conn = sqlite3.connect('D:\GSU\Data Programming\Python Project\Final Project - Video Games\python_omegA.sqlite')


df = pd.read_sql_query("SELECT * FROM videogames", conn)


# In[3]:

# Read in the table with headers
#df = pd.read_csv("D:/GSU/Data Programming/Python Project/Final Project - Video Games/Video_Games_Sales_with_ratings_dataset.csv", header=0)
# First, get rid of games missing ratings
dfsub = df[df.Rating.notnull()]
dfsub.head()


# In[4]:

dfsub.groupby(df['Rating']).count()


# In[5]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Use boolean mask, but use logical_not to invert it
mask = np.logical_not(dfsub['Rating'].isin(['AO','EC','K-A', 'RP']))
# filter out those unwanted games
dfsub = dfsub[mask]
# sanity check
dfsub['Rating'].unique()


# In[6]:

# group by rating and look at the total Sales numbers
df_group = dfsub[['NA_Sales','EU_Sales','JP_Sales','Global_Sales','Other_Sales']].groupby(dfsub['Rating']).sum()
df_group


# In[7]:

import seaborn as sns
f, (ax1, ax2) = plt.subplots(1,2, figsize=(10,5))
sns.countplot(x="Rating", data=dfsub, palette="Greens_d", ax=ax1)
ax1.set_ylabel("Number of Games")
sns.barplot(x="Rating", y="Global_Sales",data=dfsub, estimator=sum, ax=ax2, ci=None)
ax2.set_ylabel("Total Global Sales (millions)")


# In[ ]:



