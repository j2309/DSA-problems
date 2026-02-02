# to find second largest number in a list
def secondlargest(numbers): #1.make function
    unique_num=list(set(numbers)) #2. remove duplicates by converting the set to the list 
    unique_num.sort() #3. sort the list small to large
    return unique_num[-2]#4.return the second largest number

print(secondlargest([10,20,30,40,50,60,70,80,40,55,60])) #5.print it




# using largest variable 
def secondlargest(self,nums):
    largest=nums[0]
    second_largest=-1
    for num in nums:
        if num>largest:
            second_largest =largest
            num=largest
       elif num >second_largest and num!=largest:
           num = second largest
  return second_largest
