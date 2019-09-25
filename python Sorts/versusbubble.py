import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv('bubble_C++.txt',sep = ",",names=['Size','Time'])
df1 = pd.read_csv('bubble_Java.txt',sep = ",",names=['Size','Time'])
df2 = pd.read_csv('bubble_Python.txt',sep = ",",names=['Size','Time'])
x=df.iloc[:,0]
y=df.iloc[:,1]
x2 = df.iloc[:,0]
y1 = df1.iloc[:,1]
y2 = df2.iloc[:,1]

##########################################################
plt.plot(x,y,color="red",label="Bubble Sort C++")
plt.plot(x,y1,color="blue",label="Bubble Sort Java")
plt.plot(x,y2, color="yellow", label="Bubble Sort Python")

##########################################################
plt.xlabel('Size')
plt.ylabel('Tiempo(ms)')
plt.title('Bubble Sort Versus')
plt.legend()
plt.show()