# to find the sum of pairs that equals to target
def sumofpairs(arr,target):
    pairs=[]
    seen =set()
    for num in arr:
        difference=target-num
        if difference in seen:
            pairs.append((difference,num))
        seen.add(num)
    return pairs

print(sumofpairs([1,2,3,4,5,6,7,8,9],12))    