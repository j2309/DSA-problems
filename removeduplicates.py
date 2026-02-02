# to remove duplicates from alist
def removeduplicates(numbers): #1.make function
    numbers=[1,2,3,3,4,4,5,6,7]
    seen = set()
    result=[]
    for num in numbers:
       if num not in seen:
         seen.add(num)
       else:
         result.append(num)
         return result
    
    print(result)
       
