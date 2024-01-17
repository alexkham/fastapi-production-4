from fastapi import APIRouter


router=APIRouter(
    prefix='/hexadecimal',
    tags=['hexadecimal']

)

@router.get("/add/{x}/{y}")
def add_hdecimal(x,y):
    result=int(x,16)+int(y,16)
    result=hex(result)
    
    return {"result":str(result)[2:]}

@router.get("/subtract/{x}/{y}")
def subtract_hexadecimal(x,y):
    result=int(x,16)-int(y,16)
    result=hex(result)
    
    return {"result":str(result)[2:]}

@router.get("/multiply/{x}/{y}")
def multiply_hexadecimal(x,y):
    result=int(x,16)*int(y,16)
    result=hex(result)
    
    return {"result":str(result)[2:]}


@router.get("/divide/{x}/{y}")
def divide_hexadecimal(x,y):
    result=int(x,16)//int(y,16)
    result=hex(result)
    
    return {"result":str(result)[2:]}  

