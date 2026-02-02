# to find missing number in the sequence
def missingnumber(nums): # make function
    n=len(nums)+1 #total numbers including missing number
    sum_of_n = n*(n+1)//2 # formula to calculate sum of first n numbers
    sum_of_nums=sum(nums)
    missingnumber = sum_of_n - sum_of_nums
    return missingnumber  # return the result
print(missingnumber([1,2,3,4,6,7,8])) # print it
