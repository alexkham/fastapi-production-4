from fastapi import APIRouter


router=APIRouter(
    prefix='/octal',
    tags=['octal']

)

@router.get("/add/{x}/{y}")
def add_octal(x,y):
    result=int(x,8)+int(y,8)
    result=oct(result)
    
    return {"result":str(result)[2:]}

@router.get("/subtract/{x}/{y}")
def subtract_octal(x,y):
    result=int(x,8)-int(y,8)
    result=oct(result)
    
    return {"result":str(result)[2:]}

@router.get("/multiply/{x}/{y}")
def multiply_octal(x,y):
    result=int(x,8)*int(y,8)
    result=oct(result)
    
    return {"result":str(result)[2:]}


@router.get("/divide/{x}/{y}")
def divide_octal(x,y):
    result=int(x,8)//int(y,8)
    result=oct(result)
    
    return {"result":str(result)[2:]}  

