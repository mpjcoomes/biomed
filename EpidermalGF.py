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
import statsmodels.api as sm
import statsmodels.formula.api as smf
import scipy.stats as stats
sns.set(style='ticks', palette='bright')


# Data
df1 = pd.DataFrame({'p-EGFR' : [300214,7284816,16954164,21990500,33693732,45891900,22858634,20084782],
                   'GAPDH' : [3027240,3005640,3451124,2926244,4321660,3507678,2474334,2472444]})
df2 = pd.DataFrame({'p-EGFR' : [96472,3174818,6898440,9709753,13339992,18482520,8033086,9062368],
                   'GAPDH' : [1318186,1507386,1630128,1967688,1865396,1758405,1241733,1540788]})
df3 = pd.DataFrame({'p-EGFR' : [161418,5814219,9600054,13507779,18553811,32141925,11177212,12607914],
                   'GAPDH' : [1921501,2806489,1777100,2051308,3021122,2855405,2237231,2735917]})
df1['Norm'] = df1['p-EGFR']/df1['GAPDH']
df2['Norm'] = df2['p-EGFR']/df2['GAPDH']
df3['Norm'] = df3['p-EGFR']/df3['GAPDH']
df = pd.DataFrame({'BLOT 1' : df1['Norm']/df1['Norm'][0],
                   'BLOT 2' : df2['Norm']/df2['Norm'][0],
                   'BLOT 3' : df3['Norm']/df3['Norm'][0]})
df.index = [0,1,5,15,30,60,720,1440]
df = df.stack()
df = df.reset_index()
df.columns = ['Time','Blot','Fold']


# Fig 2
ax = sns.barplot(x='Time',
                 y='Fold',
                 data=df,
                 facecolor=(1, 1, 1, 0),
                 edgecolor='0',
                 errwidth=1.25,
                 ci=68,
                 capsize=.2)
ax.set_yticks(ticks=np.arange(0,175,25))
ax.set_yticks(ticks=np.arange(25/2,150,25), minor = True)
ax.set(ylim=(0,150),
       title='p-EGFR(Tyr1173) / GADPH ratio as fold change relative to control     \n',
       xlabel='Time (min)',
       ylabel='Fold Change (a.u.)')
sns.despine()
plt.savefig('Fig_1.png',
            dpi=1000,
            bbox_inches='tight',
            transparent=True,
            pad_inches=0)
plt.show()


# Analysis
print(stats.shapiro(df['Fold']))

print(stats.levene(df[df['Time'] == 0]['Fold'],
                   df[df['Time'] == 1]['Fold'],
                   df[df['Time'] == 5]['Fold'],
                   df[df['Time'] == 15]['Fold'],
                   df[df['Time'] == 30]['Fold'],
                   df[df['Time'] == 60]['Fold'],
                   df[df['Time'] == 720]['Fold'],
                   df[df['Time'] == 1440]['Fold'],center='mean'))

gel_lm = smf.ols('Fold ~ C(Time)', data=df).fit()
print(sm.stats.anova_lm(gel_lm, typ=1))
print(gel_lm.summary())

gel_poc = sm.stats.multicomp.MultiComparison(df['Fold'],df['Time'])
gel_bonf = gel_poc.allpairtest(stats.ttest_ind, method='bonf')
print(gel_bonf[0])
