def logest_uniques_string(s):
    char_set= set()
    left=0
    right=0
    longest=0
     start=0
    for roght in range(len(s)):
       while s[right]in char_set:
          left+=1
          char_set.add(s[right])
          if right-left+1>longest:
             longest=right-left+1
             start=left
             return s[start:start+longest]
          
          srting="abcdbbb"
          result=longest_uniques_string(string)
          print("longest uniques strong the iven stgring is :",result)
