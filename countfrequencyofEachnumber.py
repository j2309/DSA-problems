#count  the frequency of each number in a list
nums=[1,2,3,4,4,4,4,5,5] # using count() method 
count=nums.count(3)
print("the frequency of number  is :",count)

              #-----OR------ 

# count the frequency of each number using dictionary
frequency={}
for num in nums:
    frequency[num]=frequency.get(num,0)+1 # get() method to get the number and increment by 1
print("the frequency of each number is :" ,frequency)
