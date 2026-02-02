def is_palindrome(s):
    s=s.lower()
    if  s==s[::-1]:
        print(f'"{s} is a palindrome"')
    else:
        print(f'"{s} is not a palindrome"')
is_palindrome("madam")
is_palindrome("janhvi")
