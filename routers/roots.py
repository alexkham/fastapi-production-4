from fastapi import APIRouter
import math
import fractions

router=APIRouter(
    prefix='/roots',
    tags=['roots']

)

@router.get("/sqrt/{x}/")
def square_root(x:str):
    try:
      result=math.sqrt(float(x))
      return {"result":str(result)} 
    except:
      return  {"result":'NaN',
              "StatusCode":500} 
    
@router.get("/cubic-root/{x}/")
async def cubic_root(x: float):
    number=float(x)
    if number >= 0:
        result = float(number ** (1/3))
    else:
        result = float(-(-number) ** (1/3))  # Handle negative numbers
    
    return {"result": str(result)} 

@router.get("/fourth-root/{x}")
async def fourth_root(x: float):
    number=float(x)
    if number >= 0:
        result = number ** (1/4)
    else:
        result = math.nan
    
    return {"result":str(result)}   
    
@router.get("/root/{x}/{y}")
def get_root(x,y):
    degree=float(x)
    number=float(y)
    result=number**(1/degree)
    return {"result":str(result)}      
