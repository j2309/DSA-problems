# to find sum of all numbers in the list
def sumofnumbers(numlist):
    total=0
    for num in numlist:
        total+=num
    return total
print("the sum of the list :",end="")
print(sumofnumbers([1,2,3,4,5]))