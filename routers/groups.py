from fastapi import APIRouter
import re


router=APIRouter(
    prefix='/groups',
    tags=['groups']

)


@router.get("/prime/{x}")
def primarity_check(x):
    result=is_prime_str(x)
    return { "result":result}



def is_prime_str(input_str):
    try:
        number = int(input_str)  # Try to convert the input string to an integer
        if float(input_str) != number:
            return False  # Input is a float, not an integer
        if number <= 1:
            return False
        if number <= 3:
            return True

        if number % 2 == 0 or number % 3 == 0:
            return False

        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                return False
            i += 6

        return True
    except ValueError:
        return False  # Not a number

# Example usage:
# input_str = "17"  # You can pass any string as input
# result = is_prime_str(input_str)
# if result is True:
#     print(f"{input_str} is a prime number.")
# elif result is False:
#     print(f"{input_str} is not a prime number or not an integer.")
# else:
#     print(f"{input_str} is a float, not an integer.")

@router.get("/odd_or_even/{x}")
def odd_or_even(x):
    if  "." in str(x):
        return { "result":"The number is not integer"}
    else:         
      try:
        number = int(x)  # Try to convert the input string to an integer
        
        if is_even(number):
            return { "result":"Even"}
        else:
            return { "result":"Odd"}
      except ValueError:
        return { "result":"NaN"}

def is_even(number):
    if number%2==0:
        return True
    else:
        return False
    
@router.get("/perfect_square/{x}")
def perfect_square(x):
    number=int(x)
    if number < 0:
        return False  # Negative numbers are not perfect squares
    sqrt = int(number ** 0.5)  # Calculate the integer square root
    return sqrt * sqrt == number  # Check if the square of the square root equals the number


def is_nan(input_str):
    return input_str.lower() == "nan"

def is_float_number(input_str):
    try:
        float_value = float(input_str)
        return "." in input_str and float_value != int(float_value)
    except ValueError:
        return False  # Not a floating-point numberq