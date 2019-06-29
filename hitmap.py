import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('first.csv',sep=';')

fig = plt.figure()

ax = fig.add_subplot(1,1,1)
data = np.random.rand(4,2)
rows = list('1234')
columns = list('MF')
fig.ax = plt.subplot()
ax.pcolor(data,cmap=plt.cm.Reds,edgecolors='k')
ax.set_xticks(np.arange(0,2)+0.5)
ax.set_yticks(np.arange(0,4)+0.5)
ax.xaxis.tick_bottom()
ax.yaxis.tick_left()
ax.set_xticklabels(columns,minor=False,fontsize=20)
ax.set_yticklabels(rows,minor=False,fontsize=20)
plt.show()