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
      number=float(x)
      if number < 0:
        return { "result":False}  # Negative numbers are not perfect squares
      
      sqrt = int(number ** 0.5)  # Calculate the integer square root
      result=sqrt * sqrt == number# Check if the square of the square root equals the number
      return   {"result" :result}
    except:
        return {"result":"Invalid input: NaN"}


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

@router.get("/perfect_cube/{x}")
def perfect_cube(x):
    try:
     number=float(x)
     cube_root = round(number ** (1/3))
     result=cube_root ** 3 == number
     return {"result":result}
    except:
        return {"result":"Invalid input: Not Integer"}
    
@router.get("/perfect_number/{x}")
def is_perfect_number(x):
    """
    Check if a given number is a perfect number.

    Parameters:
    number (int): The number to be checked.

    Returns:
    bool: True if the number is a perfect number, False otherwise.
    """
    try:
     number=int(x)
     if number <= 1:
        result=False
        return {"result":result}

    # Find the divisors of the number
     divisors = [1]
     for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            divisors.extend([i, number // i])
     result=sum(divisors) == number
    # Check if the sum of divisors is equal to the original number
     return {"result":result}
    except:
        return {"result":"Invalid input"}

# Example usage:
# number = 28  # 28 is a perfect number
# if is_perfect_number(number):
#     print(f"{number} is a perfect number.")
# else:
#     print(f"{number} is not a perfect number.")
@router.get("/irrational_number/{x}")
def is_irrational_from_string(x):
    """
    Check if a given number (provided as a string) is irrational.

    Parameters:
    number_str (str): The number as a string to be checked.

    Returns:
    bool: True if the number is irrational, False if it's rational, None if it's not a valid number representation.
    """
    try:
        number = float(x)  # Convert the string to a float
    except ValueError:
        return {"result":"Invalid input"}  # Not a valid number representation

    try:
        number.as_integer_ratio()  # Attempt to convert the number to a rational fraction
        return False  # Number is rational
    except OverflowError:
        return True  # Number is irrational

# Example usage:
# number_str = "ksjjbhbh"  # This is not a valid number representation
# result = is_irrational_from_string(number_str)
# if result is None:
#     print(f"{number_str} is not a valid number representation.")
# elif result:
#     print(f"{number_str} is an irrational number.")
# else:
#     print(f"{number_str} is a rational number.")
 
@router.get("/is_fibonacci/{x}")
def is_fibonacci(x):
    """
    Check if a given number is part of the Fibonacci sequence.

    Parameters:
    number (int): The number to be checked.

    Returns:
    bool: True if the number is in the Fibonacci sequence, False otherwise.
    """
    
    try:
        number=int(x)
        if number < 0:
            return False  # Negative numbers are not part of the Fibonacci sequence
        elif number <= 1:
            return True  # 0 and 1 are part of the Fibonacci sequence
        else:
            a, b = 0, 1
            while a < number:
                a, b = b, a + b
                result=a == number
            return {"result":result}
    except:
        return {"result":"Invalid input"}

# Example usage:
# number = 8  # 8 is part of the Fibonacci sequence (0, 1, 1, 2, 3, 5, 8, ...)
# if is_fibonacci(number):
#     print(f"{number} is part of the Fibonacci sequence.")
# else:
#     print(f"{number} is not part of the Fibonacci sequence.")
@router.get("/is_triangular/{x}")
def is_triangular(x):
    """
    Check if a given number is a triangular number.

    Parameters:
    number (int): The number to be checked.

    Returns:
    bool: True if the number is a triangular number, False otherwise.
    """
    try:
        number=int(x)
        if number < 0:
            return False  # Negative numbers are not triangular

        total = 0
        n = 1
        while total < number:
            total += n
            if total == number:
                result=True
                return {"result":result}
            n += 1
            result=False
        return  {"result":result}
    except:
        return {"result":"Invalid input"}

# Example usage:
# number = 21  # 21 is a triangular number (1 + 2 + 3 + 4 + 5 + 6 = 21)
# if is_triangular(number):
#     print(f"{number} is a triangular number.")
# else:
#     print(f"{number} is not a triangular number.")
