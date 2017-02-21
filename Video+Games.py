
# coding: utf-8

# In[2]:

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

#df=pd.dataframe()
df=pd.read_csv('C:\Users\Prathamesh\Desktop\Video.csv')
df1=pd.read_csv('C:\Users\Prathamesh\Desktop\Video.csv')


# In[3]:

from matplotlib.pyplot import hist
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
fig=plt.figure(figsize=(8, 6), dpi= 100, facecolor='w', edgecolor='k')
a=df.groupby('Platform').agg(sum)['Global_Sales'].plot.bar()
fig=plt.figure(figsize=(4, 3), dpi= 60, facecolor='w', edgecolor='k')
b=df.groupby('Platform').agg(sum)['NA_Sales'].plot.bar()
fig=plt.figure(figsize=(4, 3), dpi= 60, facecolor='w', edgecolor='k')
c=df.groupby('Platform').agg(sum)['EU_Sales'].plot.bar()


# In[ ]:

fig=plt.figure(figsize=(18, 16), dpi= 80, facecolor='w', edgecolor='k')


# In[6]:

from matplotlib.pyplot import hist
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(10, 8), dpi= 80, facecolor='w', edgecolor='k')
get_ipython().magic(u'matplotlib inline')
df.groupby('Genre').agg(sum)['Global_Sales'].plot.bar()


# In[13]:

from matplotlib.pyplot import hist
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
fig=plt.figure(figsize=(10, 8), dpi= 80, facecolor='w', edgecolor='k')
df.groupby('Year_of_Release').agg(sum)['Global_Sales'].plot.bar()


# In[36]:

import matplotlib.pyplot as plt

# the portion you want to dedicate to each value
# for example for first one is 5 out of 43 makes it %11.6
result0 = pd.DataFrame(df.groupby(['Name'], as_index = False).agg({'Global_Sales':sum}).sort('Global_Sales', ascending=False))[0:5]
result1 = pd.DataFrame(df.groupby(['Name'], as_index = False).agg({'NA_Sales':sum}).sort('NA_Sales', ascending=False))[0:5]
result2 = pd.DataFrame(df.groupby(['Name'], as_index = False).agg({'EU_Sales':sum}).sort('EU_Sales', ascending=False))[0:5]
result3 = pd.DataFrame(df.groupby(['Name'], as_index = False).agg({'JP_Sales':sum}).sort('JP_Sales', ascending=False))[0:5]
result4 = pd.DataFrame(df.groupby(['Name'], as_index = False).agg({'Other_Sales':sum}).sort('Other_Sales', ascending=False))[0:5]

values0 = [float(i) for i in result0.Global_Sales]
values1 = [float(i) for i in result1.NA_Sales]
values2 = [float(i) for i in result2.EU_Sales]
values3 = [float(i) for i in result3.JP_Sales]
values4 = [float(i) for i in result4.Other_Sales]

values=[values0,values1,values2,values3,values4]

colors = ['b', 'g', 'r', 'c', 'm']
labels0 = [str(i) for i in result0.Name]
labels1 = [str(i) for i in result1.Name]
labels2 = [str(i) for i in result2.Name]
labels3 = [str(i) for i in result3.Name]
labels4 = [str(i) for i in result4.Name]

labels=[labels0,labels1,labels2,labels3,labels4]
title=['Global Sales','Sales in North America','Sales in Europe','Sales in Japan','Rest of th World']

# move the second value section out of the chart. The higher the number the farther it gets moved
explode = (0.1, 0, 0, 0, 0)

for i in range(0,5):
# autopct the %.1f is Python formating and %% used to show as percent
    plt.figure(i)
    if(i==0):
        fig=plt.figure(figsize=(10, 8), dpi= 80, facecolor='w', edgecolor='k')
    else:
        fig=plt.figure(figsize=(5, 3), dpi= 60, facecolor='w', edgecolor='k')
    plt.pie(values[i], colors=colors, labels=labels[i], 
            explode=explode, autopct='%.1f%%',
            counterclock=False, shadow=True)
    plt.title(title[i])



plt.show()


# In[30]:




# In[ ]:



