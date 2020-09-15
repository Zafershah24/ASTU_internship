import pandas as pd
import numpy as np

import datetime

df=pd.read_csv('uber.csv')

print(df['START_DATE*'])


df['START_DATE*'] = pd.to_datetime(df['START_DATE*'])
df['END_DATE*'] = pd.to_datetime(df['END_DATE*'])

df['Travel Time']=df['END_DATE*']-df['START_DATE*']
df['Travel Time(mins)']=df[:]['Travel Time'] / np.timedelta64(1, 'm')
#Dropping the last row since it has all null values and is not required
df=df.drop(df.tail(1).index, inplace=True)

# Finding out avg speed
df['Average Speed(miles/min)'] = df['MILES*']/df['Travel Time(mins)']
# from IPython.display import display
# import matplotlib.pyplot as plt
# plt.scatter(df['MILES*'], df['Travel Time(mins)'])
# plt.show()

import seaborn as sns

sns.heatmap(df.isnull(),yticklabels=False)

# Looking at the SNS plot for null values, we can see that the column PURPOSE* has lot of NULL values
# So we can drop that Column
df=df.drop(['PURPOSE*'],axis=1)


import calendar

df['START_DATE*'] = pd.to_datetime(df['START_DATE*'], format="%m/%d/%Y %H:%M")
df['END_DATE*'] = pd.to_datetime(df['END_DATE*'], format="%m/%d/%Y %H:%M")
#defining empty lists
hour=[]
day=[]
day_of_the_week=[]
weekday=[]
month=[]

for x in df['START_DATE*']:
    hour.append(x.hour) #adding/appending the values to above empty list
    day.append(x.day)
    day_of_the_week.append(x.dayofweek)
    weekday.append(calendar.day_name[day_of_the_week[-1]])
    month.append(x.month)
#creating columns
df['HOUR']=hour
df['DAY']=day
df['DAY_OF_WEEK']=day_of_the_week
df['WEEKDAY']=weekday
df['MONTH']=month

#Overall Analysis in terms of CATEGORY
df.groupby('CATEGORY*').mean().plot(kind='barh',figsize=(10,5))

# trips per hour in a day
df['HOUR'].value_counts().plot(kind='barh',figsize=(15,8),color='green')
df['HOUR'].value_counts().plot(kind='pie',figsize=(12,15),autopct='%1.1f%%')
# trips per day of week
df['WEEKDAY'].value_counts().plot(kind='barh',figsize=(15,8),color='orange')
df['WEEKDAY'].value_counts().plot(kind='pie',figsize=(12,15),autopct='%1.1f%%')
#trips per day of the month
df['DAY'].value_counts().plot(kind='barh',figsize=(15,8),color='pink')
df['DAY'].value_counts().plot(kind='pie',figsize=(12,15),autopct='%1.1f%%')


#trips in month, DECEMBER month has highest number of trips as depicted in the figure
df['MONTH'].value_counts().plot(kind='barh',figsize=(15,8),color='blue')
df['MONTH'].value_counts().plot(kind='pie',figsize=(12,15),autopct='%1.1f%%')

