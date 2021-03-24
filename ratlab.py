# -*- coding: utf-8 -*-
"""
WinPython 3.6.6.1Zero.exe
~\WPy-3661\WinPython Command Prompt.exe
python.exe -m pip install --upgrade pip
pip install spyder
pip install matplotlib
pip install pandas
pip install seaborn
pip install statsmodels
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
sns.set(style='ticks', palette='bright')
pd.set_option('display.max_columns', 10)


# Data
df = pd.DataFrame({'Open Arm (sec)' : [236,182,200,246,176,32,17,74,95,48],
Closed Arm (sec)' : [311,342,277,295,361,503,520,435,475,531],
Open Arm (entries)' : [13,14,20,16,15,5,3,7,8,5],
Closed Arm (entries)' : [15,19,25,14,20,18,21,12,13,17],
Total Entries (#)' : [25,29,19,27,23,16,29,23,21,22],
Alterations (#)' : [13,17,11,15,13,6,13,9,8,9],
Genotype' : ['WT','WT','WT','WT','WT','TG','TG','TG','TG','TG']
})

df['Total Time'] = df['Open Arm (sec)'] + df['Closed Arm (sec)']
df['Total Entries'] = df['Open Arm (entries)'] + df['Closed Arm (entries)']
df['Open Arm Time (%)'] = df['Open Arm (sec)'] / df['Total Time'] * 100
df['Open Arm Entries (%)'] = df['Open Arm (entries)'] / df['Total Entries'] * 100
df['Spontaneous Alternations (%)'] = df['Alterations (#)'] / ( df['Total Entries (#)'] - 2 ) * 100



# One-sided Mann–Whitney U test
df_p = pd.DataFrame(index = ['Open Arm Time (%)','Open Arm Entries (%)','Spontaneous Alternations (%)'])
x = df.loc[df['Genotype'] == 'WT', 'Open Arm Time (%)']
y = df.loc[df['Genotype'] == 'TG', 'Open Arm Time (%)']
df_p.loc['Open Arm Time (%)','U_Stat'], df_p.loc['Open Arm Time (%)', 'p-value'] = stats.mannwhitneyu(x,y)

x = df.loc[df['Genotype'] == 'WT', 'Open Arm Entries (%)']
y = df.loc[df['Genotype'] == 'TG', 'Open Arm Entries (%)']
df_p.loc['Open Arm Entries (%)','U_Stat'], df_p.loc['Open Arm Entries (%)', 'p-value'] = stats.mannwhitneyu(x,y)

x = df.loc[df['Genotype'] == 'WT', 'Total Entries']
y = df.loc[df['Genotype'] == 'TG', 'Total Entries']
df_p.loc['Total Entries','U_Stat'], df_p.loc['Total Entries', 'p-value'] = stats.mannwhitneyu(x,y)

x = df.loc[df['Genotype'] == 'WT', 'Spontaneous Alternations (%)']
y = df.loc[df['Genotype'] == 'TG', 'Spontaneous Alternations (%)']
df_p.loc['Spontaneous Alternations (%)','U_Stat'], df_p.loc['Spontaneous Alternations (%)', 'p-value'] = stats.mannwhitneyu(x,y)

df_p['p-value-adj'] = np.where(df_p['p-value'] * 4 <= 1, df_p['p-value'] * 4, 1)



# Power Analysis
df.groupby(['Genotype']).mean()
np.sqrt(df.groupby(['Genotype']).var())



# Fig 1. Emotional Dysregulation: Open arm time or entries percentage
f, (ax1, ax2) = plt.subplots(1,2)
ax = sns.barplot(x = 'Genotype',
y = 'Open Arm Time (%)',
data = df,
facecolor = (1, 1, 1, 0),
edgecolor = '0',
errwidth = 1.25,
ci = 68,
capsize = .2,
ax=ax1)
ax.set_yticks(ticks=np.arange(0,60,10))
ax.set_yticks(ticks = np.arange(0,50,2), minor = True)
ax = sns.barplot(x = 'Genotype',
y = 'Open Arm Entries (%)',
data = df,
facecolor = (1, 1, 1, 0),
edgecolor = '0',
errwidth = 1.25,
ci = 68,
capsize = .2,
ax=ax2)
ax.set_yticks(ticks = np.arange(0,50,2), minor = True)
ax.set(title = 'Mean percentage open arm time or entries over total time or entries by genotype                                                                  \n')
sns.despine()
plt.savefig('Fig_1.png',
dpi=1000,
bbox_inches='tight',
transparent=True,
pad_inches=0)
plt.show()



# Fig 2. Cognitive Decline: motor activity and spontaneous alterations
f, (ax1, ax2) = plt.subplots(1,2)
ax = sns.barplot(x = 'Genotype',
y = 'Total Entries',
data = df,
facecolor = (1, 1, 1, 0),
edgecolor = '0',
errwidth = 1.25,
ci = 68,
capsize = .2,
ax=ax1)
ax.set_yticks(ticks=np.arange(0,50,10))
ax.set_yticks(ticks = np.arange(0,40,2), minor = True)
ax = sns.barplot(x = 'Genotype',
y = 'Spontaneous Alternations (%)',
data = df,
facecolor = (1, 1, 1, 0),
edgecolor = '0',
errwidth = 1.25,
ci = 68,
capsize = .2,
ax=ax2)
ax.set_yticks(ticks=np.arange(0,80,10))
ax.set_yticks(ticks = np.arange(0,70,2), minor = True)
ax.set(title = 'Mean total entries and percentage spontaneous alternations by genotype                                                                  \n')
sns.despine()
plt.savefig('Fig_2.png',
dpi=1000,
bbox_inches='tight',
transparent=True,
pad_inches=0)
plt.show()
