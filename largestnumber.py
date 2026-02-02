#find largets number in the list
def largestnumber(numlist):
   numlist.sort()
   return (numlist[-1])
print(" the largest number in the list is :",largestnumber([1,3,2,4,6,5,7,8]))
