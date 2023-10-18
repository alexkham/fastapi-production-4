from fastapi import APIRouter
import math
import fractions
from typing import List
from pydantic import BaseModel
import statistics


router=APIRouter(
    prefix='/fractions',
    tags=['fractions']

)

@router.get("/frac/{x}/")
def frac(x):
    result=fractions.Fraction(float(x))
    return {"result":str(result)}