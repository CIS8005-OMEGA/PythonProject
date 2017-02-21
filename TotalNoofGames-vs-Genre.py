
# coding: utf-8

# In[1]:

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().magic(u'matplotlib inline')
sns.set()
pd.set_option('display.max_rows',16)
pd.set_option('display.max_columns',100)
plt.style.use('ggplot')

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

from subprocess import check_output
# Any results you write to the current directory are saved as output.


# In[2]:

import sqlite3
import pandas as pd
conn = sqlite3.connect('D:\GSU\Data Programming\Python Project\Final Project - Video Games\python_omegA.sqlite')


df = pd.read_sql_query("SELECT * FROM videogames", conn)
print(df)


# In[3]:

df.shape


# In[5]:

len(df.Name.unique())


# In[7]:

df.isnull().sum()


# In[9]:

multiple_platform_title = df.groupby('Name').agg({'Name':lambda x : len(x) if (len(x) > 1) else None}).dropna()
multiple_platform_title.Name = multiple_platform_title.Name.astype(np.int64)
multiple_platform_title = multiple_platform_title.sort_values(['Name'], ascending=False)
multiple_platform_title.columns = ['Platform_count']
multiple_platform_title


# In[11]:

cols = ['Name','Platform','Year_of_Release','Publisher']
df.loc[df.Name=='Need for Speed: Most Wanted', cols].sort_values(['Year_of_Release'])


# In[13]:

# games based on genre
games_by_genre = df.groupby('Genre').agg({'Genre':len}).sort_values('Genre')
plt.subplots(figsize=(10,7))
ax = sns.pointplot(x=games_by_genre.index, y=games_by_genre.Genre)
ax.set_title('Total Number of Games by Genre', color='blue', size=25, alpha=0.5)
ax.set_xlabel('Genre', color='green', size=25, alpha=0.5)
ax.set_ylabel('Total Number of Games', color='green', size=25, alpha=0.5)


# In[ ]:



