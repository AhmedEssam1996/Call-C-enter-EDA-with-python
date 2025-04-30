#=====================
#   import library
#====================='

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

#==================='
#   import data
#==================='

data=pd.read_excel(r"C:\Users\Elbostan\Desktop\call\Call-Center.xlsx")

#======================='
#   Data preprocessing.
#======================='

data.info()

data.isna().sum()

"fill null columns"

data[['Satisfaction rating', 'AvgTalkDuration', 'Speed of answer in seconds']] = data[['Satisfaction rating', 'AvgTalkDuration', 'Speed of answer in seconds']].fillna(0)


describe=data.describe()
plt.figure(figsize=(10, 6))
sns.heatmap(describe,annot=True, cmap="coolwarm", linewidths=0.5)
plt.show()

#=============================================================='
#                        Data Analysis
#=============================================================='

"                     Overall customer satisfaction ?                                          "

satisfaction_percentage = data['Satisfaction rating'].value_counts(normalize=True) * 100
plt.pie(satisfaction_percentage.values, labels=satisfaction_percentage.index, autopct='%1.1f%%', startangle=90)
plt.title("satisfaction percentage")
plt.show()

sns.barplot(x=satisfaction_percentage.index, y=satisfaction_percentage.values)
plt.ylabel('satisfaction percentage')
plt.show()



"                    Overall calls answered/abandoned  ?                      "

sns.countplot(data=data, x='Answered (Y/N)')
plt.show()


"                           Calls by time                                     "

data['Date'] = pd.to_datetime(data['Date'])
data['DateTime'] = data.apply(lambda row: pd.to_datetime(str(row['Date'].date()) + ' ' + row['Time'].strftime('%H:%M:%S')), axis=1)
data['Hour'] = data['DateTime'].dt.hour
calls_by_hour = data.groupby('Hour')['Call Id'].count().reset_index()
calls_by_hour.rename(columns={'Call Id': 'Number of Calls'}, inplace=True)

sns.barplot(data=calls_by_hour, x='Hour', y='Number of Calls')
plt.title("calles by hours")
plt.xlabel("hours")
plt.ylabel("calles answers")
plt.xticks(rotation=45)
plt.show()















