import requests
import json


# binary_conversions=[]

# def int_to_binary(x:int):
#     result=bin(x)
#     return str(result)[2:]


# for i in range(100001):
#     intNum=i
#     binNum=int_to_binary(i)
#     binary_conversions.append(binNum)

# with open('int_to_binary.json', 'w') as file:
#     json.dump(binary_conversions,file,indent=4)
    
#------------------------------------------------------------------

# def int_to_hexadecimal(x:int):
#     result=hex(x)
#     return str(result)[2:]

# hexadecimal_conversions=[]

# for i in range(100001):
#     intNum=i
#     hexNum=int_to_hexadecimal(i)
#     hexadecimal_conversions.append(hexNum.upper())

# with open('int_to_hexadecimal.json', 'w') as file:
#     json.dump(hexadecimal_conversions,file,indent=4)
    

#----------------------------------------------------------------    
    
# def int_to_octal(x:int):
#     result=oct(x)
#     return str(result)[2:]

# octal_conversions=[]

# for i in range(100001):
#     intNum=i
#     octNum=int_to_octal(i)
#     octal_conversions.append(octNum)

# with open('int_to_octal.json', 'w') as file:
#     json.dump(octal_conversions,file,indent=4)

#-----------------------------------------------------------------


    

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

primes=[]
for i in range(1,10000):
    if is_prime_str(str(i)):
        primes.append(i)


primes        

