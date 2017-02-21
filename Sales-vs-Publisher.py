
# coding: utf-8

# In[6]:

import sqlite3
import pandas as pd
conn = sqlite3.connect('D:\GSU\Data Programming\Python Project\Final Project - Video Games\python_omegA.sqlite')


df = pd.read_sql_query("SELECT * FROM Videogames", conn)
print(df)


# In[2]:

dfsub = df[df.Rating.notnull()]
dfsub.head()


# In[10]:

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns

global_sales_publisher = df.pivot_table(index=['Publisher'], values=['NA_Sales','EU_Sales','JP_Sales'], 
                                           aggfunc=np.sum).sort_values(['NA_Sales'], ascending=False)
global_sales_publisher = global_sales_publisher[['NA_Sales','EU_Sales','JP_Sales']]
ax = global_sales_publisher.iloc[0:10,:].plot(kind='bar', stacked=True, grid=False)
ax.set_title('Top 10 Publishers by Sales', size=25, color='blue', alpha=0.5)
ax.set_xlabel('Publisher', size=25, color='green', alpha=0.5)
ax.set_ylabel('Sales', size=25, color='green', alpha=0.5)
plt.show()


# In[ ]:



