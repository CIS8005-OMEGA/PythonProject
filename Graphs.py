
# coding: utf-8

# In[ ]:

import pandas as pd
from matplotlib.pyplot import hist
df = pd.read_csv('C:\Users\Admin\Downloads\Video_Games_Sales_as_at_22_Dec_2016.csv')
df.groupby('Genre').agg(sum)['Global_Sales'].plot.bar()


# In[38]:

import pandas as pd
get_ipython().magic(u'matplotlib inline')
from matplotlib.pyplot import hist
df = pd.read_csv('C:\Users\Admin\Downloads\Video_Games_Sales_as_at_22_Dec_2016.csv')
s=['Global_Sales','NA_Sales','EU_Sales','JP_Sales','Other_Sales']
for i in range(0,5):
    s1 = df.groupby(['Genre','Year_of_Release']).agg(sum)[s[i]]
    del s1['Adventure']
    del s1['Strategy']
    del s1['Simulation']
    del s1['Fighting']
    del s1['Racing']
    del s1['Misc']
    if i>0:
        ax = s1.unstack('Genre').plot(kind = "line",figsize=(7.5,6),title=""+s[i]+" Video Games Sales by Genre Per Year")
    else:
        ax = s1.unstack('Genre').plot(kind = "line",figsize=(16,10),title=""+s[i]+" Video Games Sales by Genre Per Year")
    ax.set(xlabel="Years", ylabel="Net Sales")


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# 

# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



