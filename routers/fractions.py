from fastapi import APIRouter
import math
import fractions
from fractions import Fraction
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



@router.get("/mixed/")
def simplify_mixed_fraction(whole_fraction: str):
    try:
        fraction = Fraction(whole_fraction)
        numerator = fraction.numerator
        denominator = fraction.denominator

        if denominator == 0:
            return {"error": "Denominator cannot be zero"}

        if numerator == 0:
            return {"result": "0"}  # Handle cases where the fraction is zero.

        integer_part, remainder = divmod(abs(numerator), denominator)

        if numerator < 0:
            sign = "-"
        else:
            sign = ""

        if remainder == 0:
            return {"result": f"{sign}{integer_part}"}
        else:
            return {"result": f"{sign}{integer_part} {remainder}/{denominator}"}
    except ValueError:
        return {"error": "Invalid input"}

# Example usage:
# Access the endpoint with a query parameter `whole_fraction`.
# Example URL: /simplify_mixed_fraction?whole_fraction=3 1/4

@router.get("/inverse/{x}/")
def inverse(x):
    x=float(x)
    if x==0:
        return {"result": 'NaN', "StatusCode": 500}
    result=1/x
    return {"result":str(result)}
