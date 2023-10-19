from fastapi import APIRouter
import math
import fractions

router=APIRouter(
    prefix='/logs',
    tags=['logarithms']

)


@router.get("/log10/{x}/")
def log10(x):
    result=math.log10(float(x))
    return {"result":str(result)}

@router.get("/log2/{x}/")
def log2(x):
    result=math.log2(float(x))
    return {"result":str(result)}


@router.get("/loganybase/{x}/{y}")
def get_log_any_base(x,y):
    base=float(x)
    number=float(y)
    result=math.log(number,base)
    return {"result":str(result)}  

@router.get("/natural/{x}/")
def log(x):
    result=math.log(float(x))
    return {"result":str(result)}