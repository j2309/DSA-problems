# Moore Voting Algorithm - there should be two variable ( element ,count) then lets assume element is our answer and iterate throughout the array and increse the count when prev=next element and decrese when prev!= next element by one.
#1. brute force- Using i and j  and itrate . TC-O(n^2) SC-O(1)
#2. better idea - use Hashing technique (key:value) TC:O(n log n + n), SC:O(n)
#3. optimal idea- apply moore voting algorithms 

def majority_element_1(self,nums):
  n=len(nums)
  count=0, element=0
  for num in nums:
    if count == 0:
      count =1
      element= num
    elif element==num:
      count+=1
    else:
      count-=1
      count=nums.count(element)
      if count > n^2:
        return element
  return -1
