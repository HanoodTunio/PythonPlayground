# this program will find the elements which are common in both list

list1 = list(("Apple", "Mango", "Banana", "Grapes","Peach","Papaya", "Pomegranate"))
list2 =list(("Pomegranate", "Olive", "Guava", "Pineapple", "Watermelon", "Apple"))
commonList = []

for x in range(len(list1)):
    for y in range(len(list2)):
        if list1[x]==list2[y]:
            commonList.append(list1[x])

print("The common elements between the list are: ", commonList)

