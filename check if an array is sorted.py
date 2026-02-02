class Solution:
    def isSorted(self, nums):
        for num in  nums:
            if num > num-1: # obviously, if the array is sorted , previous value is smaller than next value.
                return true
            else: 
                return  false
        return true 

arr={1,3,4,5,9}
n=len(arr)
print(isSorted)
