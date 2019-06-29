import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('first.csv',sep=';')
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
"""
var = df.groupby('MI').Sales.sum()

ax1.set_xlabel('BMI')
ax1.set_ylabel('sum of sales ')
ax1.set_title('BMI wise sum of sales')
var.plot(kind='line')
#plt.show()

var = df.groupby(['MI','Gender']).Sales.sum()
var.unstack().plot(kind='bar',stacked=True,color=['red','blue'],grid=False)
#plt.show()
var = df.groupby(['Gender','MI']).Sales.sum()
var.unstack().plot(kind='bar',stacked=True,color=['red','blue','green','black'],grid=False)
#plt.show()
"""

ax.scatter(df['Age'],df['Sales'])
ax.set_title('age avec ventes')
#plt.show()
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(df['Age'],df['Sales'],s=df['Income'])
ax.set_title('age avec vente avec revenues de la perssone')
plt.show()

