# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 09:18:39 2019

@author: rlangran
"""

#import modules
import matplotlib.pyplot as plt
import pandas as pd
import os
import seaborn as sns

#Set filename and filepath
filename = 'results2.xlsx'
filepath = os.path.join(r'C:\Users\rlangran\Desktop\UT Data Analytics\Section 5',filename)

#Import dataset
df = pd.read_csv('default of credit card clients.csv', header =1)

#change name of default field
df.rename(columns={'default payment next month':'DEFAULT_IND'}, inplace=True)

#Inspect general characteristics of the dataset
print(df.head())

print(df.describe())

print(df.info())

## Next Steps before EDA
#•	Data cleaning
#•	Data transformation
#•	How to deal with missing values?
#•	Data reduction
#•	Data discretization
#•	Text cleaning (if needed)

#Data reduction
#Consolidate the other education indicators into one
#“0, 4, 5, 6” all other school
#1 - graduate school
#2 - university
#3 - high school
#4 - others
df['EDUCATION'] = df['EDUCATION'].replace(0,4).replace(5,4).replace(6,4)

#Create a single late payment indicator
#“-2” no payment required / “-1” paid in full / “0” partial payment / “1,2,3,…” number of months payment is past due
#PAY_0	PAY_2	PAY_3	PAY_4	PAY_5	PAY_6
#"1" indicator = has had a late payment / "0" indicator = has not had a late payment
Nme1 = []
for row in df.itertuples():
    if row.PAY_0 > 0 or row.PAY_2 > 0 or row.PAY_3 > 0 or row.PAY_4 > 0 or row.PAY_5 > 0 or row.PAY_6 > 0:
        lpi = 1
    else:
        lpi = 0
    
    Nme1.append(lpi)
    
    
df['LATE_PMT'] = Nme1

#Data discretizing
#Age: 21-79 -4 bins 0-29,30-45,46-59,60-79
bins = [0, 30, 45, 60, 100]
labels = ['1','2','3','4']
df['AGE_BIN'] = pd.cut(df['AGE'], bins=bins, labels=labels)

#Calculated fields
#Average Balance and Average Payment Amt

df['AVG_BAL'] = df.iloc[:,12:18].mean(axis=1)
df['AVG_PMT'] = df.iloc[:,18:24].mean(axis=1) 

df['DIFF'] = df['AVG_BAL'] - df['AVG_PMT']

#Ratio of Avg Pmt to Avg Bal
df['PMT_RTO'] = df['AVG_PMT'] / df['AVG_BAL']


df['PMT_RTO'] = df['PMT_RTO'].apply(lambda x: round(x,3))
df['DIFF'] = df['DIFF'].apply(lambda x: round(x,0))  

## EXPLORATORY DATA ANALYSIS XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

header = df.dtypes.index
print(header)

#plt.hist(df['LIMIT_BAL'], bins=4)
#plt.show()

fig1, ax1 = plt.subplots()
ax1.set_title('AGE HISTOGRAM')
ax1.hist(df['AGE_BIN'], bins=4, color='mediumblue',alpha=0.7, rwidth=0.85,edgecolor="k")
fig1, ax2 = plt.subplots()
ax2.set_title('CREDIT LIMIT HISTOGRAM')
ax2.hist(df['LIMIT_BAL'], bins=4, color='mediumblue',alpha=0.7, rwidth=0.85,edgecolor="k")
fig1, ax3 = plt.subplots()
ax3.set_title('EDUCATION HISTOGRAM')

#Set education to string
df['EDU'] = df['EDUCATION'].astype(str)
ax3.hist(df['EDU'], bins=4, color='mediumblue',alpha=0.7, rwidth=0.85,edgecolor="k")

fig1, ax4 = plt.subplots()
ax4.set_title('MARRIAGE HISTOGRAM')

#Set education to string
df['MAR'] = df['MARRIAGE'].astype(str)
ax4.hist(df['MAR'], bins=4, color='mediumblue',alpha=0.7, rwidth=0.85,edgecolor="k")

fig1, ax5 = plt.subplots()
ax5.set_title('GENDER HISTOGRAM')

#Set education to string
df['GEN'] = df['SEX'].astype(str)
ax5.hist(df['GEN'], bins=4, color='mediumblue',alpha=0.7, rwidth=0.85,edgecolor="k")

#Histogram for three calc fields
#AVG_BAL:
bins = [-60000, 0, 75000, 150000, 1000000]
df['AVB_BIN'] = pd.cut(df['AVG_BAL'], bins=bins, labels=labels)

fig1, ax6 = plt.subplots()
ax6.set_title('AVG BAL HISTOGRAM')
ax6.hist(df['AVB_BIN'], bins=4, color='mediumblue',alpha=0.7, rwidth=0.85,edgecolor="k")

#AVG_PMT:
bins = [0, 5000, 10000, 20000, 700000]
labels = ['1','2','3','4']
df['AVP_BIN'] = pd.cut(df['AVG_PMT'], bins=bins, labels=labels)
fig1, ax7 = plt.subplots()
ax7.set_title('AVG PMT HISTOGRAM')
ax7.hist(df['AVP_BIN'], bins=4, color='mediumblue',alpha=0.7, rwidth=0.85,edgecolor="k")

#fig1, ax8 = plt.subplots()
#ax8.set_title('AVG PMT RATIO HISTOGRAM')
#ax8.hist(df['PMT_RTO'], bins=4, color='mediumblue',alpha=0.7, rwidth=0.85)
fig1, ax8 = plt.subplots()
ax8.set_title('CREDIT LIMIT')
ax8.plot(df['LIMIT_BAL'])

#x = df['PAY_0']
#y = df['PAY_2']
#fig1, ax9 = plt.subplots()
#ax9.set_title('SCATTER PLOT-PMT_0 VS PMT_2')
#ax9.scatter(x,y)

x = df['AVG_PMT']
y = df['AVG_BAL']
fig1, ax9 = plt.subplots()
ax9.set_title('SCATTER PLOT-AVG PMT VS AVG BAL')
ax9.scatter(x,y)

fig = plt.figure()
ax11 = fig.add_subplot(211)
ax21 = fig.add_subplot(212)

sns.regplot(x=df['AVG_PMT'], y=df['AVG_BAL'], data=df, fit_reg=False, color='mediumblue',marker="+",x_jitter=.05,ax=ax11)
g = sns.regplot(x=df['AGE'], y=df['AVG_BAL'], data=df, fit_reg=False, color='mediumblue',marker="+",x_jitter=.05,ax=ax21)


fig = sns.FacetGrid(df, hue='DEFAULT_IND', aspect=4)
fig.map(sns.kdeplot, 'AGE', shade=True)
oldest = df['AGE'].max()
fig.set(xlim=(0,oldest))
fig.set(title='Distribution of Age Grouped by Default Indicator')
fig.add_legend()

fig = sns.FacetGrid(df, hue='LATE_PMT', aspect=4)
fig.map(sns.kdeplot, 'AGE', shade=True)
oldest = df['AGE'].max()
fig.set(xlim=(0,oldest))
fig.set(title='Distribution of Age Grouped by Late Payment Indicator')
fig.add_legend()

#problem with ID 28717 paid 3.764M but balance was 1.093M
newdf = df[(df['DIFF']<=0) & (df['LATE_PMT']==0)]

len(newdf)

fig2, ax1 = plt.subplots()
ax1.set_title('AGE HISTOGRAM')
#AGE BIN:
#1 - 20-30
#2 - 30-45
#3 - 45-60
#4 - 60-80
ax1.hist(newdf['AGE_BIN'], bins=4, color='mediumblue',alpha=0.7, rwidth=0.85,edgecolor="k")
fig2, ax2 = plt.subplots()
ax2.set_title('CREDIT LIMIT HISTOGRAM')
ax2.hist(newdf['LIMIT_BAL'], bins=4, color='mediumblue',alpha=0.7, rwidth=0.85,edgecolor="k")
fig2, ax3 = plt.subplots()
ax3.set_title('EDUCATION HISTOGRAM')

#Set education to string
ax3.hist(newdf['EDU'], bins=4, color='mediumblue',alpha=0.7, rwidth=0.85,edgecolor="k")

#default indicator
#age 30-45
#diff 0 or less
#late_pmt 0

blue_diamond = dict(markerfacecolor='b', marker='D')
fig3, ax1 = plt.subplots()
ax1.set_title('DIFF BOXPLOT')
ax1.boxplot(df['DIFF'], flierprops=blue_diamond, vert=False, whis=0.75)

fig3, ax2 = plt.subplots()
ax2.set_title('AGE BOXPLOT')
ax2.boxplot(df['AGE'], flierprops=blue_diamond, vert=False, whis=0.75)


#Use subset for correlation and covariance
dfanl = (df[['SEX','EDUCATION','MARRIAGE','AGE','DIFF','AVG_BAL','LATE_PMT','DEFAULT_IND']])
corrMat = dfanl.corr()
print(corrMat)

covMat = dfanl.cov()
print(covMat)

writer = pd.ExcelWriter(filepath)
df.to_excel(writer,sheet_name='credit_data',index=False)
corrMat.to_excel(writer,sheet_name='corrMat',index=False)
covMat.to_excel(writer,sheet_name='covMat',index=False)

#writer.save()



