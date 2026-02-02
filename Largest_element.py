# Largest element in the array
class Solution:
    def largestElement(self, nums):
# lets assume  first element is largest 
        largest = nums[0]
compare largest value with other index in the array 
        for num in nums[1:]:
            if largest < num:
       # if num is bigger than large then power goes to that num 
                largest = num
            #print largest 
        return largest
