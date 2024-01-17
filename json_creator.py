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
    
def int_to_octal(x:int):
    result=oct(x)
    return str(result)[2:]

octal_conversions=[]

for i in range(100001):
    intNum=i
    octNum=int_to_octal(i)
    octal_conversions.append(octNum)

with open('int_to_octal.json', 'w') as file:
    json.dump(octal_conversions,file,indent=4)
    
