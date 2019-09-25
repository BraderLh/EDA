import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('quick_C++.txt',sep = ",",names=['Size','Time'])
df1 = pd.read_csv('quick_Java.txt',sep = ",",names=['Size','Time'])
df2 = pd.read_csv('quick_Python.txt',sep = ",",names=['Size','Time'])
x=df.iloc[:,0]
y=df.iloc[:,1]
y1 = df1.iloc[:,1]
y2 = df2.iloc[:,1]

##########################################################
plt.plot(x,y,color="pink",label="Quick Sort C++")
plt.plot(x,y1,color="violet",label="Quick Sort Java")
plt.plot(x,y2, color="purple", label="Quick Sort Python")

##########################################################
plt.xlabel('Size')
plt.ylabel('Tiempo(ms)')
plt.title('Quick Sort Versus')
plt.legend()
plt.show()