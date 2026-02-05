# check if the pair with given sum exists in array 
# given an array of int and a target value. return indices/ yes /no if pair exists .
def checksum():
  left =0 right =0
  while (left<right):
    sum =left+right
    if (sum == target ):
      return yes
    elif sum >target:
      right--
    else:
      left ++
return no
