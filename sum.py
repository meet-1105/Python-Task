list1 = [4, 5, 2, 8, 9, 10, 2, 34, 5, 6]

def sumOfList(list, size):
    if(size == 0):
        return 0
    else:
        return list[size-1] + sumOfList(list, size-1)

total = sumOfList(list1, len(list1))
print("Sum of all elements in given list: ", total)  
