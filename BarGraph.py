import pandas as pd
%matplotlib inline
from matplotlib.pyplot import hist
df = pd.read_csv('C:\Users\Admin\Downloads\Video_Games_Sales_as_at_22_Dec_2016.csv')

fig=plt.figure(figsize=(10, 8), dpi= 100, facecolor='w', edgecolor='k')
a=df.groupby('Genre').agg(sum)['Global_Sales'].plot.bar()
a.set_xlabel('Genre',size=10)
a.set_ylabel('Sales',size=10)

fig=plt.figure(figsize=(10, 6), dpi= 100, facecolor='w', edgecolor='k')
sub1 = plt.subplot(2, 2, 1)
sub1=df.groupby('Genre').agg(sum)['NA_Sales'].plot.bar()
sub1.set_xlabel('NA_SALES',size=10)

sub2 = plt.subplot(2, 2, 2)
sub2=df.groupby('Genre').agg(sum)['EU_Sales'].plot.bar()
sub2.set_xlabel('EU_SALES',size=10)


sub3 = plt.subplot(2, 2, 3)
sub3=df.groupby('Genre').agg(sum)['JP_Sales'].plot.bar()
sub3.set_xlabel('JP_SALES',size=10)


sub4 = plt.subplot(2, 2, 4)
sub4=df.groupby('Genre').agg(sum)['Other_Sales'].plot.bar()
sub4.set_xlabel('REST OF WORLD',size=10)


fig.tight_layout()
plt.show()