from fastapi import APIRouter


router=APIRouter(
    prefix='/binary',
    tags=['binary']

)

@router.get("/add/{x}/{y}")
def add_binary(x,y):
    result=int(x,2)+int(y,2)
    result=bin(result)
    
    return {"result":str(result)[2:]}

@router.get("/subtract/{x}/{y}")
def subtract_binary(x,y):
    result=int(x,2)-int(y,2)
    result=bin(result)
    
    return {"result":str(result)[2:]}

@router.get("/multiply/{x}/{y}")
def multiply_binary(x,y):
    result=int(x,2)*int(y,2)
    result=bin(result)
    
    return {"result":str(result)[2:]}


@router.get("/divide/{x}/{y}")
def divide_binary(x,y):
    result=int(x,2)//int(y,2)
    result=bin(result)
    
    return {"result":str(result)[2:]}  

