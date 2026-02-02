#to find factorial of a number using recursion
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
number=int(input("enter the number for finding its factorial:"))
print("the factorial of the number is:",factorial(number))
        
        # ----- OR-----
 
  # to show the fatorial like 5!=5*4*3*2*1=120
factorial_string = str(number)+"! = "
for i in range(number,0,-1):
    if i != 1:
        factorial_string += str(i)+"*"
    else:
        factorial_string += str(i)+" = "+str(factorial(number))

print(factorial_string)