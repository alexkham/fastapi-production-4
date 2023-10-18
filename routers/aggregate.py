from fastapi import APIRouter
import math
import fractions
from typing import List
from pydantic import BaseModel
import statistics


router=APIRouter(
    prefix='/aggregate',
    tags=['aggregate']

)

class NumbersInput(BaseModel):
    numbers: List[float]


@router.post("/sum")
def calculate_sum(numbers_input: NumbersInput):
    result = sum(numbers_input.numbers)
    return {"result": result}    

@router.post("/min")
def calculate_min(numbers_input: NumbersInput):
    result = min(numbers_input.numbers)
    return {"result": result}    

@router.post("/max")
def calculate_max(numbers_input: NumbersInput):
    result = max(numbers_input.numbers)
    return {"result": result}    

@router.post("/mean")
def calculate_mean(numbers_input: NumbersInput):
    result = sum(numbers_input.numbers)/len(numbers_input.numbers)
    return {"result": result}   

@router.post("/median")
def calculate_median(numbers_input: NumbersInput):
    result =statistics.median(numbers_input.numbers)
    return {"result": result}     