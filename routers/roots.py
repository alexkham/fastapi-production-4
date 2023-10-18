from fastapi import APIRouter
import math
import fractions

router=APIRouter(
    prefix='/roots',
    tags=['roots']

)

@router.get("/sqrt/{x}/")
def square_root(x):
    try:
      result=math.sqrt(float(x))
      return {"result":str(result)} 
    except:
      return  {"result":'NaN',
              "StatusCode":500} 
    
@router.get("/root/{x}/{y}")
def get_root(x,y):
    degree=float(x)
    number=float(y)
    result=number**(1/degree)
    return {"result":str(result)}      
