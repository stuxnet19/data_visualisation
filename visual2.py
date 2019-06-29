import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('first.csv',sep=';')
var = df.groupby('Gender').Sales.sum()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('Gender')
ax1.set_ylabel('sum of sales')
ax1.set_title('Gender wise sum of sales')
var.plot(kind='bar')
plt.show()

