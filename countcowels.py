# to count vowels in a string
def countvowels(s):
    vowels ='aeiouAEIOU'
    count=0
    for char in s :
        if char in vowels:
            count += 1
    return count
print(" the number of vowels in the string is :",countvowels("Hello there,how are you?"))
