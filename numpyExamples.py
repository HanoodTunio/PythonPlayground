from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

#generate randomly 1d array with the given probability values
arr = random.choice([1, 2, 3, 4, 5], p=[0.0, 0.2, 0.3, 0.2, 0.3], size=(50))
print(arr)

#generate 2d array with the given probability values
arr2 = random.choice([1, 2, 3, 4], p= [0.5, 0.3, 0.2, 0], size=(3, 5))
print(arr2)

# permutation in array using the shuffle or permutation method
arr3 = np.array([1,2,3,4,5])
print(random.permutation(arr3))


# plot graph
#plt.subplot(1, 2, 1)
arr4 = np.array([0,1,2,3,4,5,6,7,8])
sn.distplot(arr4)
plt.show()

# plotting a graph without histogram 
arr5 = np.array([0,1,2,3,4,5,6,7,8,9])
sn.distplot(arr5, hist=False)
plt.show()

