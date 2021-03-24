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
df = pd.DataFrame({'JR Carb (g)' : [0.007,0.002,0.009,0.018,0.816,1.604,1.684,2.083,1.163,np.NaN,np.NaN,np.NaN,np.NaN],
MJ Carb (g)' : [0.011,0.018,0.134,0.253,0.417,0.588,0.881,1.000,0.802,np.NaN,np.NaN,np.NaN,np.NaN],
DD Carb (g)' : [0.001,0.015,0.026,0.084,0.260,0.689,1.036,1.135,1.132,np.NaN,np.NaN,np.NaN,np.NaN],
JA Carb (g)' : [0.011,0.008,0.017,0.020,0.330,0.915,1.210,1.242,0.858,np.NaN,np.NaN,np.NaN,np.NaN],
AP Carb (g)' : [0.001,0.007,0.062,0.090,0.153,0.568,0.731,0.719,0.428,np.NaN,np.NaN,np.NaN,np.NaN],
SO Carb (g)' : [0.039,0.042,0.156,0.367,0.998,2.135,2.333,1.841,1.961,np.NaN,np.NaN,np.NaN,np.NaN],
JA CarbX (g)' : [0.000,0.002,0.009,0.021,0.066,0.198,0.325,0.835,1.365,1.559,np.NaN,np.NaN,np.NaN],
MJ CarbX (g)' : [0.027,0.039,0.089,0.112,0.162,0.355,0.576,0.774,1.117,1.183,np.NaN,np.NaN,np.NaN],
AL CarbX (g)' : [0.003,0.003,0.022,0.023,0.063,0.086,0.138,0.478,0.993,1.311,np.NaN,np.NaN,np.NaN],
AP CarbX (g)' : [0.008,0.019,0.048,0.037,0.033,0.120,0.378,0.515,0.738,1.050,np.NaN,np.NaN,np.NaN],
TJ CarbX (g)' : [0.020,0.041,0.059,0.085,0.136,0.257,0.373,0.778,1.649,2.079,np.NaN,np.NaN,np.NaN],
AH CarbY (g)' : [0.304,0.274,0.912,1.290,1.826,2.369,2.878,3.099,3.403,4.031,np.NaN,np.NaN,np.NaN],
HE CarbY (g)' : [0.014,0.055,0.085,0.168,0.440,0.768,1.076,0.839,1.224,0.401,np.NaN,np.NaN,np.NaN],
SY CarbY (g)' : [0.290,0.370,0.569,0.638,1.321,1.601,1.724,1.587,1.761,1.941,np.NaN,np.NaN,np.NaN],
ZM CarbY (g)' : [0.200,0.230,0.310,0.448,0.953,1.083,1.171,1.236,1.821,2.069,np.NaN,np.NaN,np.NaN],
SJ CarbY (g)' : [0.041,0.022,0.117,0.243,0.388,0.453,0.361,1.840,2.490,2.320,np.NaN,np.NaN,np.NaN],
ZM Hist (g)' : [0.001,0.104,0.146,0.300,0.439,0.563,0.599,0.717,0.686,np.NaN,np.NaN,np.NaN,np.NaN],
AL Hist (g)' : [0.014,0.023,0.026,0.058,0.118,0.185,0.780,1.329,1.674,np.NaN,np.NaN,np.NaN,np.NaN],
AP Hist (g)' : [0.006,0.024,0.012,0.053,0.239,0.638,0.918,1.058,1.018,np.NaN,np.NaN,np.NaN,np.NaN],
SO Hist (g)' : [0.006,0.009,0.085,0.013,0.281,1.250,1.740,2.067,2.059,np.NaN,np.NaN,np.NaN,np.NaN],
JA HistX (g)' : [0.200,0.345,0.625,0.832,1.156,1.457,1.548,1.634,1.599,1.525,np.NaN,np.NaN,np.NaN],
JR HistX (g)' : [0.273,0.350,0.562,0.911,1.531,1.957,2.362,2.538,2.675,2.419,np.NaN,np.NaN,np.NaN],
AL HistX (g)' : [0.111,0.172,0.242,0.416,0.791,1.251,1.466,1.637,1.599,1.795,np.NaN,np.NaN,np.NaN],
AP HistX (g)' : [0.198,0.160,0.263,0.472,0.566,1.145,1.118,1.090,1.135,1.186,np.NaN,np.NaN,np.NaN],
CZ HistX (g)' : [0.035,0.037,0.031,0.052,0.096,0.093,0.212,0.220,0.265,0.240,np.NaN,np.NaN,np.NaN],
TJ HistX (g)' : [0.071,0.101,0.120,0.225,0.383,0.754,1.038,1.431,1.607,1.699,np.NaN,np.NaN,np.NaN],
SY HistY (g)' : [-0.001,0.010,0.003,0.001,0.012,0.023,0.036,0.028,0.133,0.156,0.286,0.335,0.340],
AH HistY (g)' : [0.009,0.035,0.123,0.067,0.152,0.231,0.213,0.500,0.708,1.026,1.390,1.631,1.709],
HE HistY (g)' : [0.008,-0.001,-0.002,-0.020,0.045,0.043,0.121,0.242,0.528,0.669,0.990,1.207,1.316],
ZM HistY (g)' : [0.013,0.014,0.014,0.020,0.020,0.025,0.053,0.145,0.199,0.231,0.297,0.365,0.398]
})
for i in range(0,len(df.columns)):
df[df.columns.str.replace('g', '%')[i]] = df.iloc[:,i]/df.iloc[:,i][df.iloc[:,i].idxmax()]*100
df.index = [1.00E-08,2.00E-08,5.00E-08,1.00E-07,2.00E-07,5.00E-07,1.00E-06,2.00E-06,5.00E-06,1.00E-05,2.00E-05,5.00E-05,1.00E-04]
df = df.stack()
df = df.reset_index()
df.columns = ['Concentration','Sample','Response']
conds = ['Carbachol','Carb+Atro','Carb+Mepy','Histamine','Hist+Atro','Hist+Mepy']
df['Drug'] = ''
for i, j in zip([' Carb ',' CarbX ',' CarbY ',' Hist ',' HistX ',' HistY '], conds):
df['Drug'] = np.where(df['Sample'].str.contains(i), j, df['Drug'])

# Models
df['Concentration'] = np.log10(df['Concentration'])
df_reg = df[df['Sample'].str.contains('%')]
df_reg = df_reg.reset_index()
for i in conds:
for j in df_reg.loc[:,'Sample'].drop_duplicates():
logic = (df_reg['Drug'] == i) & (df_reg['Sample'] == j)
z = df_reg.loc[logic].copy()
z.loc[z['Response'].diff() < 0, 'Response'] = np.NaN
x = z.loc[z['Response'].between(10, 90), 'Concentration']
y = z.loc[z['Response'].between(10, 90), 'Response']
if y.empty:
pass
else:
slope, intercept = stats.linregress(x, y)[:2]
df_reg.loc[logic, 'Slope'] = slope
df_reg.loc[logic, 'Intercept'] = intercept
df_reg.loc[logic, 'Line'] = intercept + slope * z.loc[:,'Concentration']

# EC50 and fold change
df_reg['EC50'] = (50-df_reg['Intercept'])/df_reg['Slope']
df_reg['EC50_pow'] = 10 ** df_reg['EC50']
fold = df_reg.loc[:,['Drug','EC50_pow']].groupby(['Drug']).mean()
fold.loc[['Carb+Atro', 'Carb+Mepy'], 'Fold_Change'] = fold.loc[['Carb+Atro', 'Carb+Mepy'], 'EC50_pow'] / float(fold.loc['Carbachol', 'EC50_pow'])
fold.loc[['Hist+Atro', 'Hist+Mepy'], 'Fold_Change'] = fold.loc[['Hist+Atro', 'Hist+Mepy'], 'EC50_pow'] / float(fold.loc['Histamine', 'EC50_pow'])

# Statistical Tests
EC50 = df_reg.loc[:,['Drug','EC50_pow']].drop_duplicates()
EC50 = EC50.set_index('Drug')
x = EC50.loc['Carbachol', 'EC50_pow']
y = EC50.loc['Carb+Atro', 'EC50_pow']
z = EC50.loc['Carb+Mepy', 'EC50_pow']
fold.loc['Carbachol','U_H_Stats'], fold.loc['Carbachol', 'p-value'] = stats.kruskal(x,y,z)
fold.loc['Carb+Atro','U_H_Stats'], fold.loc['Carb+Atro', 'p-value'] = stats.mannwhitneyu(x,y)
fold.loc['Carb+Mepy','U_H_Stats'], fold.loc['Carb+Mepy', 'p-value'] = stats.mannwhitneyu(x,z)
x = EC50.loc['Histamine', 'EC50_pow']
y = EC50.loc['Hist+Atro', 'EC50_pow']
z = EC50.loc['Hist+Mepy', 'EC50_pow']
fold.loc['Histamine','U_H_Stats'], fold.loc['Histamine', 'p-value'] = stats.kruskal(x,y,z)
fold.loc['Hist+Atro','U_H_Stats'], fold.loc['Hist+Atro', 'p-value'] = stats.mannwhitneyu(x,y)
fold.loc['Hist+Mepy','U_H_Stats'], fold.loc['Hist+Mepy', 'p-value'] = stats.mannwhitneyu(x,z)
fold['p-value-adj'] = np.where(fold['p-value'] * 8 <= 1, fold['p-value'] * 8, 1)
print(fold)
Eff = df.loc[df['Sample'].str.contains('g'), ['Drug', 'Response', 'Sample']].groupby(['Sample','Drug']).max().reset_index()
Eff = Eff.loc[:,['Drug','Response']].set_index('Drug')
x = Eff.loc['Carbachol', 'Response']
y = Eff.loc['Carb+Atro', 'Response']
z = Eff.loc['Carb+Mepy', 'Response']
Eff.loc['Carbachol','U_H_Stats'], Eff.loc['Carbachol', 'p-value'] = stats.kruskal(x,y,z)
x = Eff.loc['Histamine', 'Response']
y = Eff.loc['Hist+Atro', 'Response']
z = Eff.loc['Hist+Mepy', 'Response']
Eff.loc['Histamine','U_H_Stats'], Eff.loc['Histamine', 'p-value'] = stats.kruskal(x,y,z)
Eff['p-value-adj'] = np.where(Eff['p-value'] * 8 <= 1, Eff['p-value'] * 8, 1)
print(Eff.loc[-np.isnan(Eff['U_H_Stats']), Eff.columns != 'Response'].drop_duplicates())

# Figure 1
ax = sns.lineplot(x = 'Concentration',
y = 'Response',
hue = 'Drug',
style = 'Drug',
data = df[df['Sample'].str.contains('%') & df['Drug'].str.contains('Carb')],
aa = True,
clip_on = False,
markers = True,
lw = 1,
dashes = False,
ci = 68,
err_style = 'bars',
estimator = 'mean',
)
for i, j in zip(['Carbachol','Carb+Mepy','Carb+Atro'], ['blue', 'lime', 'orange']):
x = df_reg.loc[df_reg['Drug'] == i, 'Concentration'].drop_duplicates()
y = df_reg.loc[df_reg['Drug'] == i].groupby(['Drug', 'Concentration']).mean().reset_index()['Line']
plt.plot(x, y, linewidth = 1, color=j, linestyle = '--')
ax.set(xlim = (-8.1,-4.8),
ylim = (0,100),
title = 'Mean response of guinea pig ileum to Carbachol and antagonists        \n',
xlabel = 'log [Carbachol] (M)',
ylabel = 'Response (%) '
)
ax.minorticks_on()
sns.despine()
plt.savefig('Fig_1.png',
dpi = 1000,
bbox_inches = 'tight',
pad_inches = 0)
plt.show()

# Figure 2
ax = sns.lineplot(x = 'Concentration',
y = 'Response',
hue = 'Drug',
style = 'Drug',
data = df[df['Sample'].str.contains('%') & df['Drug'].str.contains('Hist')],
aa = True,
clip_on = False,
markers = True,
lw = 1,
dashes = False,
ci = 68,
err_style = 'bars',
estimator = 'mean',
)
for i, j in zip(['Histamine','Hist+Mepy','Hist+Atro'], ['blue', 'lime', 'orange']):
x = df_reg.loc[df_reg['Drug'] == i, 'Concentration'].drop_duplicates()
y = df_reg.loc[df_reg['Drug'] == i].groupby(['Drug', 'Concentration']).mean().reset_index()['Line']
plt.plot(x, y, linewidth = 1, color=j, linestyle = '--')
ax.set(xlim = (-8.1,-3.9),
ylim = (0,100),
title = 'Mean response of guinea pig ileum to Histamine and antagonists        \n',
xlabel = 'log [Histamine] (M)',
ylabel = 'Response (%) '
)
ax.minorticks_on()
sns.despine()
plt.savefig('Fig_2.png',
dpi = 1000,
bbox_inches = 'tight',
pad_inches = 0)
plt.show()
