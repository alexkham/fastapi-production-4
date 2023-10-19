from fastapi import APIRouter
import math
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

@router.get("/subtract/{x}/{y}")
def subtract(x,y):
    result=float(x)-float(y)
    
    return {"result":str(result)}

@router.get("/multiply/{x}/{y}")
def multiply(x,y):
    result=float(x)*float(y)
    
    return {"result":str(result)}

@router.get("/divide/{x}/{y}")
def divide(x,y):
    try:
      result=float(x)/float(y)
      return {"result":str(result)}
    except:
      return {"result":'NaN',
              "StatusCode":500}  
    
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
    x=float(x)
    y=float(y)
    result=math.fmod(x,y)
    return {"result":str(result)}      

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