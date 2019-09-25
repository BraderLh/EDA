import matplotlib.pyplot as plt
import bubbleSort as bubbleSort
import selectionSort as selectionSort
import heapSort as heapSort
import insertionSort as insertionSort
import mergeSort as mergeSort
import countingSort as countingSort
import quickSort as quickSort
from tryItABunch import tryItABunch

nValuesb, tValuesb = tryItABunch( bubbleSort.bubble_sort, startN = 50, endN = 1050, stepSize=50, numTrials=10, listMax = 20 )
'''nValuess, tValuess = tryItABunch( selectionSort.selection_sort, startN = 50, endN = 1050, stepSize=50, numTrials=10, listMax = 20)
nValuesi, tValuesi = tryItABunch( insertionSort.insertion_sort, startN = 50, endN = 1050, stepSize=50, numTrials=10, listMax = 20)
nValuesh, tValuesh = tryItABunch( heapSort.heap_sort, startN = 50, endN = 1050, stepSize=50, numTrials=10, listMax = 20)
nValuesm, tValuesm = tryItABunch( mergeSort.merge_sort, startN = 50, endN = 1050, stepSize=50, numTrials=10, listMax = 20)
nValuesc, tValuesc = tryItABunch( countingSort.counting_sort, startN = 50, endN = 1050, stepSize=50, numTrials=10, listMax = 20)
nValuesq, tValuesq = tryItABunch( quickSort.quick_sort, startN = 50, endN = 1050, stepSize=50, numTrials=10, listMax = 20)
#plt.plot(nValuesNaive, tValuesNaive, color="red", label="Bubble Sort")'''
plt.plot(nValuesb, tValuesb, color="red", label="Bubble Sort")
'''plt.plot(nValuess, tValuess, color="blue", label="Selection Sort")
plt.plot(nValuesi, tValuesi, color="green", label="Insertion Sort")
plt.plot(nValuesh, tValuesh, color="yellow", label="Heap Sort")
plt.plot(nValuesm, tValuesm, color="black", label="Merge Sort")
plt.plot(nValuesc, tValuesc, color="purple",label="Counting Sort")
plt.plot(nValuesq, tValuesq, color="brown", label="Quick Sort")'''

plt.xlabel("n")
plt.ylabel("Time(ms)")
plt.legend()
plt.title("Versus Sorts Python")
plt.show()