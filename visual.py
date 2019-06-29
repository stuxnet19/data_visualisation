import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("first.csv",sep=';')
print(df)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.hist(df['Age'],bins = 4)
ax.boxplot(df['Age'])
plt.title('Age distribution')
plt.xlabel('Age')
plt.ylabel('#Employee')
plt.show()
