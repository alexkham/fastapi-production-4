from fastapi import APIRouter
import math


router=APIRouter(
    prefix='/constants',
    tags=['constants']

)

@router.get("/pi/")
def get_pi():
    result=math.pi    
    return {"result":str(result)}  

@router.get("/e/")
def get_e():
    result=math.e    
    return {"result":str(result)}  

@router.get("/tau/")
def get_tau():
    result=math.tau    
    return {"result":str(result)}  