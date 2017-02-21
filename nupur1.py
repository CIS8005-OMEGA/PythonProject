import sqlite3
import pandas as pd
import numpy as np # linear algebra
import matplotlib.pyplot as plt
import seaborn as sns
conn = sqlite3.connect('C:\Users\Nupur Chhabra\Documents\MSIS\data programming-python\project\project_videogames.sqlite')

df = pd.read_sql_query("SELECT * FROM Videogames", conn)

platform_name = df.Platform.value_counts()

plt.subplots(figsize=(10,10))
ax = sns.barplot(x=platform_name , y=platform_name .index, palette='cubehelix')
ax.set_title('Most Number of games per Platform', color='black', alpha=0.7, size=30)
ax.set_xlabel('Total Titles', color='black', alpha=0.7, size=40)
ax.set_ylabel('Platform', color='black', alpha=0.7, size=40)

plt.show()