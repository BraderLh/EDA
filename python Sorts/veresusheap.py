import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('heap_C++.txt',sep = ",",names=['Size','Time'])
df1 = pd.read_csv('heap_Java.txt',sep = ",",names=['Size','Time'])
df2 = pd.read_csv('heap_Python.txt',sep = ",",names=['Size','Time'])
x=df.iloc[:,0]
y=df.iloc[:,1]
y1 = df1.iloc[:,1]
y2 = df2.iloc[:,1]

##########################################################
plt.plot(x,y,color="blue",label="Heap Sort C++")
plt.plot(x,y1,color="brown",label='Heap Sort Java')
plt.plot(x,y2, color="yellow", label="Heap Sort")

##########################################################
plt.xlabel('Size')
plt.ylabel('Tiempo(ms)')
plt.title('Heap Sort Versus')
plt.legend()
plt.show()