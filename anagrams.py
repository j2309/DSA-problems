# to check if the string is anagram of eachother
def anagrams(str1,str2):
  return sorted(str1.lower())==sorted(str2.lower())
str1= input("enter the first string:")
str2=input("enter the second string:")
if anagrams(str1,str2):
    print(" the strings are anagrams of eachother")
else:
    print(" the strings are not anagrams")

