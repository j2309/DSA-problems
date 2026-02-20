# return true , if there is duplicate else return false.
#1. brute force idea - using 2 pointer one is i and other is j , will give TC =O(n^2) bcz of i and j loops ,SC=O(1)constant.
#2.better idea- by doing Sorting in begining will reduce time by O(n log n ) and space is constant .
#3. optimal solution - using Hash set()  method to store unique values , it gives O(n) for space and time complexity.

def has_duplicate():
  
  if len(uniques)<len(Original):
    print("array contains duplicate")
return len(set(nums))<len(nums)
