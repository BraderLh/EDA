import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('counting_C++.txt',sep = ",",names=['Size','Time'])
#nValuesb, tValuesb = tryItABunch( bubbleSort.bubble_sort, startN = 50, endN = 10000, stepSize=50, numTrials=10, listMax = 20)
df1 = pd.read_csv('counting_Java.txt',sep = ",",names=['Size','Time'])
df2 = pd.read_csv('counting_Python.txt',sep = ",",names=['Size','Time'])
x=df.iloc[:,0]
y=df.iloc[:,1]
y1 = df1.iloc[:,1]
y2 = df2.iloc[:,1]

##########################################################
plt.plot(x,y,color="red",label="Counting Sort C++")
plt.plot(x,y1,color="black",label="Counting Sort Java")
plt.plot(x,y2, color="orange", label="Counting Sort Pyhton")

##########################################################
plt.xlabel('Size')
plt.ylabel('Tiempo(ms)')
plt.title('Counting Sort Versus')
plt.legend()
plt.show()