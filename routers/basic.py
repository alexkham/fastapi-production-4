from fastapi import APIRouter
from math import *

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