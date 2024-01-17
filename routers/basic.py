from fastapi import APIRouter
import math
from math import floor, ceil
import fractions
import random

router=APIRouter(
    prefix='/basic',
    tags=['basic_math']

)


@router.get("/add/{x}/{y}")
def add(x,y):
    result=float(x)+float(y)
    
    return {"result":str(result)}

@router.get("/add_binary/{x}/{y}")
def add_binary(x,y):
    result=int(x,2)+int(y,2)
    result=bin(result)
    
    return {"result":str(result)}

@router.get("/subtract/{x}/{y}")
def subtract(x,y):
    result=float(x)-float(y)
    
    return {"result":str(result)}

@router.get("/subtract_binary/{x}/{y}")
def subtract_binary(x,y):
    result=int(x,2)-int(y,2)
    result=bin(result)
    
    return {"result":str(result)}

@router.get("/multiply/{x}/{y}")
def multiply(x,y):
    result=float(x)*float(y)
    
    return {"result":str(result)}

@router.get("/multiply_binary/{x}/{y}")
def multiply_binary(x,y):
    result=int(x,2)*int(y,2)
    result=bin(result)
    
    return {"result":str(result)}

@router.get("/divide/{x}/{y}")
def divide(x,y):
    try:
      result=float(x)/float(y)
      return {"result":str(result)}
    except:
      return {"result":'NaN',
              "StatusCode":500}


@router.get("/divide_binary/{x}/{y}")
def divide_binary(x,y):
    result=int(x,2)//int(y,2)
    result=bin(result)
    
    return {"result":str(result)}     
    
@router.get("/power/{x}/{y}")
def power(x,y):
    result=float(x)**float(y)
    
    return {"result":str(result)}    

@router.get("/abs/{x}/")
def get_abs(x):
    result=abs(float(x))
    return {"result":str(result)}


@router.get("/percentage/{x}/{y}")
def percentage(x,y):
    result=(float(x)/float(y))*100
    return {"result":str(result)+"%"}  


    
@router.get("/modulo/{x}/{y}")
def modulo(x,y):
    x=int(x)
    y=int(y)
    result=math.fmod(x,y)
    return {"result":str(result)} 

@router.get("/lcm/{a}/{b}")
def get_lcm(a: int, b: int):
    result=abs(a*b) // math.gcd(a, b)
    return {"result":result }

@router.get("/quotient/{a}/{b}")
def get_quotient(a: int, b: int):
    result=int(a//b)
    return {"result":result }


@router.get("/gcd/{x}/{y}")
def greatest_common_divisor(x,y):
    x=int(x)
    y=int(y)
    result=math.gcd(x,y)
    return {"result":str(result)}  

@router.get("/exp/{x}/")
def exponent(x):
    result=math.exp(float(x))
    return {"result":str(result)}


@router.get("/factorial/{x}")
def get_factorial(x):
    try:
        x = float(x)  # Convert input to a floating-point number
        if x.is_integer() and x >= 0:
            result = math.factorial(int(x))
            return {"result": str(result)}
        else:
            return {"result": 'NaN', "StatusCode": 500}
    except ValueError:
        return {"result": 'NaN', "StatusCode": 500}



@router.get("/trunc/{x}/")
def get_trunc(x):
    result=math.trunc(float(x))
    return {"result":str(result)}

@router.get("/random_int/")
def get_random(x=0,y=100):
    result=random.randint(int(x),int(y))
    
    return {"result":str(result)}  

@router.get("/random_float/")
def get_random(x=0,y=100):
    result=random.uniform(float(x),float(y))
    
    return {"result":str(result)}  


@router.get("/inverse/{x}/")
def inverse(x):
    x=float(x)
    if x==0:
        return {"result": 'NaN', "StatusCode": 500}
    result=1/x
    return {"result":str(result)}


@router.get("/round/{num}")
def round_num(num: float):
   result= round(num)
   return{"result":str(result)}

@router.get("/floor/{num}")
def floor_num(num: float):
    result=floor(num)
    return{"result":str(result)}

@router.get("/ceil/{num}")
def ceil_num(num: float):
   result= ceil(num)
   return{"result":str(result)}


@router.get("/negate/{num}")
def negate(num: float):
    result= -num
    return{"result":str(result)}
