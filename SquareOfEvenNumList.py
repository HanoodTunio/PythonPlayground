
# Create a function that takes a list of integers and returns a new list with the 
#squared values of the even numbers.

import math
import random


list1 = [random.randint(1, 10) for _ in range(10)]
#print(list1)
def squareOfEven(dupList):
    sqList=[]
    for x in range(len(dupList)):
        if dupList[x]%2 == 0 :
            sqList.append(math.pow(dupList[x],2))


    return sqList

newList=squareOfEven(list1)
print("The new List with Squared values of even number: ")
for x in range(len(newList)):
    print(newList[x] , end="       ")