from random import randint
import time
import numpy as np
import matplotlib.pyplot as plt

def bubbleSort(A):
	for i in range(len(A)):
		for j in range(i,len(A)):
			if(A[i]>A[j]):
				A[i],A[j]=A[j],A[i]
	return A

timeBubble=[]
timeRegular=[]
for size in range (0,1000,50):
	arr1 = [randint(0,99) for x in range (0,size)]
	arr2 = [x for x in arr1]
	
	start = time.time()
	bubbleSort(arr1)
	stop =time.time()
	timeBubble.append(stop-start)

	start = time.time()
	arr2.sort()
	stop =time.time()
	timeRegular.append(stop-start)
	
for x,y in zip(timeBubble,timeRegular):
	print x,y

x = np.linspace(0, 1000)
plt.fill(x, timeBubble, 'r')
plt.grid(True)
plt.show()