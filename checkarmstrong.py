# to check whether a number is armstorng or not 
# Armstrong number is a number which is equal to the sum of (number of digits raise to  the power of  number of digits each).
def is_armstrong(number):
    num_str=str(number)
    num_digit=len(num_str)
    sum_of_powers=0
    for digit in num_str:
        sum_of_powers += int(digit) ** num_digit
    if sum_of_powers == number:
        print(f"{number} is an armstrong number")
    else:
        print(f"{number} is not an armstrong number")
is_armstrong(153)
