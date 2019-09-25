import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('bubble_Python.txt',sep = ",",names=['Size','Time'])
df1 = pd.read_csv('counting_Python.txt',sep=",",names=['Size','Times'])
df2 = pd.read_csv('heap_Python.txt',sep=",",names=['Size','Times'])
df3 = pd.read_csv('insertion_Python.txt',sep=",",names=['Size','Times'])
df4 = pd.read_csv('merge_Python.txt',sep=",",names=['Size','Times'])
df5 = pd.read_csv('quick_Python.txt',sep=",",names=['Size','Times'])
df6 = pd.read_csv('selection_Python.txt',sep=",",names=['Size','Times'])
x=df.iloc[:,0]
y=df.iloc[:,1]
y1 = df1.iloc[:,1]
y2 = df2.iloc[:,1]
y3 = df3.iloc[:,1]
y4 = df4.iloc[:,1]
y5 = df5.iloc[:,1]
y6 = df6.iloc[:,1]
##########################################################
plt.plot(x,y,color="red",label="Bubble Sort")
plt.plot(x,y1,color="blue",label='Counting Sort')
plt.plot(x,y2,color="green",label='Heap Sort')
plt.plot(x,y3,color="yellow",label='Insertion Sort')
plt.plot(x,y4,color="purple",label='Merge Sort')
plt.plot(x,y5,color="black",label='Quick Sort')
plt.plot(x,y6,color="brown",label='Selection Sort')
##########################################################
plt.xlabel('Size')
plt.ylabel('Tiempo(ms)')
plt.title('Sorts Python')
plt.legend()
plt.show()