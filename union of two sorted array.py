arr1={1,2,3,4}
arr2={4,5,6,7}
n1=arr1.size()
n2=arr2.size()
i =0,j=0
def Unionarr():
  while (i <n1 && j<n2):
    if arr1[i]<arr2[j]:
      if uniionarr.size==0 || unionarr.back()!=arr1[i]:
        unionearr.pushback(arr1[i])
      i++
    else:
      if unionarr.size==0|| unionearr.back()!=arr2[j]:
        unionearr.pushback(arr2[j])
      j++
  while (j<n2):
   if unionarr.size==0|| unionearr.back()!=arr2[j]:
        unionearr.pushback(arr2[j])
   j++
  while (i <n2):
     if unionarr.size==0|| unionearr.back()!=arr1[i]:
        unionearr.pushback(arr1[i])
     i++
return Unionarr()
