from fastapi import APIRouter
import re
import math


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
    
    # if x.isinstance('nan'):
    #     return {"result":"Invalid input: NaN"}
    # if not is_integer(x):
    #     return {"result":"Invalid input: Not Integer"}
    # if math.isnan(int(x)):
    #    return {"result":"Invalid input: NaN"}
    try:
      number=int(x)
      if number < 0:
        return { "result":False}  # Negative numbers are not perfect squares
      
      sqrt = int(number ** 0.5)  # Calculate the integer square root
      result=sqrt * sqrt == number# Check if the square of the square root equals the number
      return   {"result" :result}
    except:
        return {"result":"Invalid input: Not Integer"}


def is_nan(input_str):
    return input_str.lower() == "nan"

def is_float_number(input_str):
    try:
        float_value = float(input_str)
        return (float_value != int(float_value)) and ("." in input_str) 
    except ValueError:
        return False  # Not a floating-point numberq
    
def is_integer(input_str):
    if re.match(r'^[-+]?[0-9]+$', input_str) or re.match(r'^[-+]?[0-9]+\.0+$', input_str):
        return True
    return False