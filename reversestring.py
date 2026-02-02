#reverse the string " hello there" to "ereht olleh"
def reversestring(s): # 1. make function
 
 rev=" " #2. create empty string

 for i in s:
   rev +=i #3. concatenate each other
 return rev #4.return the result




#--- OR--
def reverseString(s):# using slicing(shorcut)
  return s[::-1]
print(reverseString("hello there")) #5.print it