from fastapi import APIRouter
import math
import fractions

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

@router.get("/sqrt/{x}/")
def square_root(x):
    try:
      result=math.sqrt(float(x))
      return {"result":str(result)} 
    except:
      return  {"result":'NaN',
              "StatusCode":500} 
    
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

@router.get("/log10/{x}/")
def log10(x):
    result=math.log10(float(x))
    return {"result":str(result)}

@router.get("/log2/{x}/")
def log2(x):
    result=math.log2(float(x))
    return {"result":str(result)}

@router.get("/root/{x}/{y}")
def get_root(x,y):
    degree=float(x)
    number=float(y)
    result=number**(1/degree)
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

@router.get("/inverse/{x}/")
def inverse(x):
    x=float(x)
    if x==0:
        return {"result": 'NaN', "StatusCode": 500}
    result=1/x
    return {"result":str(result)}

@router.get("/loganybase/{x}/{y}")
def get_log_any_base(x,y):
    base=float(x)
    number=float(y)
    result=math.log(number,base)
    return {"result":str(result)}  

@router.get("/frac/{x}/")
def frac(x):
    result=fractions.Fraction(float(x))
    return {"result":str(result)}