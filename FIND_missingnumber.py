# to find the missing number in an given array.
def missingno():
  XOR1=0;
  XOR2=0
  for i in range (:n):
    XOR1=XOR1^i
    i++
  for i in range (1:n-1):
    XOR2=XOR2^arr[i]
    XOR1=XOR1^i+1
return XOR1^XOR2
