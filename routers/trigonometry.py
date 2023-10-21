from fastapi import APIRouter
import math
import fractions

router=APIRouter(
    prefix='/trigo',
    tags=['trigonometry']

)

@router.get("/radians/{x}/")
def get_radians(x):
    result=math.radians(float(x))
    result=round(result,5)
    return {"result":str(result)}

@router.get("/sin/{x}/")
def get_sin(x):
    x=float(x)
    result=math.sin(math.radians(x))
    result=round(result,5)
    return {"result":str(result)}

def round_to_multiple(number, multiple):
    return multiple * round(number / multiple)

@router.get("/csc/{x}/")
def get_csc(x):
    x=float(x)
    result=1/(math.sin(math.radians(x)))
    result=round(result,5)
    return {"result":str(result)}


@router.get("/cos/{x}/")
def get_cos(x):
    x=float(x)
    result=math.cos(math.radians(x))
    result=round(result,5)
    return {"result":str(result)}

@router.get("/sec/{x}/")
def get_sec(x):
    x=float(x)
    result=1/(math.cos(math.radians(x)))
    result=round(result,5)
    return {"result":str(result)}

@router.get("/tan/{x}/")
def get_tan(x):
    x=float(x)
    result=math.tan(math.radians(x))
    result=round(result,5)
    return {"result":str(result)}

@router.get("/cot/{x}/")
def get_cot(x):
    x=float(x)
    result=1/(math.tan(math.radians(x)))
    result=round(result,5)
    return {"result":str(result)}