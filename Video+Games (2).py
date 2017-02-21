
# coding: utf-8

# In[6]:

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

#df=pd.dataframe()
df=pd.read_csv('C:\Users\Prathamesh\Desktop\Video.csv')
df1=pd.read_csv('C:\Users\Prathamesh\Desktop\Video.csv')


# In[29]:

from matplotlib.pyplot import hist
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')

fig=plt.figure(figsize=(10, 8), dpi= 100, facecolor='w', edgecolor='k')
a=df.groupby('Platform').agg(sum)['Global_Sales'].plot.bar()
a.set_xlabel('Platform',size=10)
a.set_ylabel('Sales',size=10)

fig=plt.figure(figsize=(7, 5), dpi= 100, facecolor='w', edgecolor='k')
sub1 = plt.subplot(2, 2, 1)
sub1=df.groupby('Platform').agg(sum)['NA_Sales'].plot.bar()
sub1.set_xlabel('NA_SALES',size=10)

sub2 = plt.subplot(2, 2, 2)
sub2=df.groupby('Platform').agg(sum)['EU_Sales'].plot.bar()
sub2.set_xlabel('EU_SALES',size=10)


sub3 = plt.subplot(2, 2, 3)
sub3=df.groupby('Platform').agg(sum)['JP_Sales'].plot.bar()
sub3.set_xlabel('JP_SALES',size=10)


sub4 = plt.subplot(2, 2, 4)
sub4=df.groupby('Platform').agg(sum)['Other_Sales'].plot.bar()
sub4.set_xlabel('REST OF WORLD',size=10)


fig.tight_layout()
plt.show()


# In[30]:

from matplotlib.pyplot import hist
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')

fig=plt.figure(figsize=(10, 8), dpi= 80, facecolor='w', edgecolor='k')
a=df.groupby('Year_of_Release').agg(sum)['Global_Sales'].plot.bar()
a.set_xlabel('Year Of Release',size=10)
a.set_ylabel('Sales',size=10)

fig=plt.figure(figsize=(9, 7), dpi= 80, facecolor='w', edgecolor='k')
sub1 = plt.subplot(2, 2, 1)
sub1=df.groupby('Year_of_Release').agg(sum)['NA_Sales'].plot.bar()
sub1.set_xlabel('NA_SALES',size=10)

sub2 = plt.subplot(2, 2, 2)
sub2=df.groupby('Year_of_Release').agg(sum)['EU_Sales'].plot.bar()
sub2.set_xlabel('EU_SALES',size=10)


sub3 = plt.subplot(2, 2, 3)
sub3=df.groupby('Year_of_Release').agg(sum)['JP_Sales'].plot.bar()
sub3.set_xlabel('JP_SALES',size=10)


sub4 = plt.subplot(2, 2, 4)
sub4=df.groupby('Year_of_Release').agg(sum)['Other_Sales'].plot.bar()
sub4.set_xlabel('REST OF WORLD',size=10)


fig.tight_layout()
plt.show()


# In[10]:

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
title=['GLOBAL SALES','SALES IN NA','SALES IN EU','SALES IN JP','REST OF WORLD']

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


# In[ ]:



