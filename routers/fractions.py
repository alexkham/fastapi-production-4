from fastapi import APIRouter , Query
import fractions
from fractions import Fraction
from decimal import Decimal
import re




router=APIRouter(
    prefix='/fractions',
    tags=['fractions']

)

@router.get("/float_to_frac/{x}/")
def frac(x):
    result=fractions.Fraction(str(x))
    return {"result":str(result)}



@router.get("/float_to_mixed/{whole_fraction}")
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
        elif integer_part==0:
            return {"result": f"{sign}{remainder}/{denominator}"}
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



@router.get("/calculate_fraction")
def convert_and_calculate_fraction(num1:str, den1:str, operation:str, num2:str, den2:str):
    # try:
        # Convert the string arguments to decimals
       

        # Convert the decimal arguments to fractions
        fraction1 = Fraction(int(num1),int(den1))
        fraction2 = Fraction(int(num2),int(den2))

        #result = None
        #explanation = []
        numerator1 = fraction1.numerator
        denominator1 = fraction1.denominator
        numerator2 = fraction2.numerator
        denominator2 = fraction2.denominator
        # result=fraction1+fraction2
        # return {"result":f"{numerator1}/{denominator1},{operation},{numerator2}/{denominator2},{result}"}

        if operation == "add":
            result = fraction1 + fraction2
        elif operation=="subtract":
            result=fraction1-fraction2 
        elif operation == "multiply":
            result = fraction1 * fraction2 
        elif operation == "divide":
            result = fraction1 / fraction2    

        num=result.numerator
        den=result.denominator
        integer_part=num/den
        fraction_part=Fraction(float(result-integer_part))
        decimal=f"{integer_part}{fraction_part}"
        mixed=simplify_mixed_fraction(result)["result"]
           
        #    # explanation.append(f"Adding {fraction1} and {fraction2}: {result}")
        return { "result": f"{result}",
                "numerator":f"{num}",
                "denominator":f"{den}",
                "decimal":f"{decimal}",
                "mixed":f"{mixed}"}   
        # elif operation == "subtract":
        #     result = fraction1 - fraction2
        #     explanation.append(f"Subtracting {fraction2} from {fraction1}: {result}")
        # elif operation == "multiply":
        #     result = fraction1 * fraction2
        #     explanation.append(f"Multiplying {fraction1} and {fraction2}: {result}")
        # elif operation == "divide":
        #     result = fraction1 / fraction2
        #     explanation.append(f"Dividing {fraction1} by {fraction2}: {result}")
        # else:
        #     explanation.append("Invalid operation")

        # return {"explanation": explanation, "result": result}
   
# @router.get("/mixed_to_float")
# def to_float(x):
#      x=str(x)
#      x=x.strip()
#      spl=re.split('\s+', x)
#      if len(spl)>1: 
#         [whole,frac]=spl
#         num = float(whole.strip()) + float(Fraction(frac.strip()))
#         return {"result":str(num)}
#      else:
#         num=float(Fraction(x.strip())) 
#         return {"result":str(num)}

@router.get("/mixed_to_float")
def mixed_to_float(x: str = Query(...)):  # 'x' is now a required query parameter
    x = x.strip()
    spl = re.split(r'\s+', x)
    if len(spl) > 1:
        whole, frac = spl
        num = float(whole) + float(Fraction(frac))
    else:
        num = float(Fraction(x))
    return {"result": str(num)}


@router.get("/add_mixed")
def add_mixed(x: str = Query(...), y: str = Query(...)):
    res1=mixed_to_float(x)
    num1=res1["result"]
    res2=mixed_to_float(y)
    num2=res2["result"]
    result=Fraction(Decimal(num1))+Fraction(Decimal(num2))
    result=simplify_mixed_fraction(result)
    return result
    # return {"result": result}


@router.get("/subtract_mixed")
def subtract_mixed(x: str = Query(...), y: str = Query(...)):
    res1=mixed_to_float(x)
    num1=res1["result"]
    res2=mixed_to_float(y)
    num2=res2["result"]
    result=Fraction(str(num1))-Fraction(str(num2))
    result=simplify_mixed_fraction(result)
    return result


@router.get("/multiply_mixed")
def multiply_mixed(x: str = Query(...), y: str = Query(...)):
    res1=mixed_to_float(x)
    num1=res1["result"]
    res2=mixed_to_float(y)
    num2=res2["result"]
    result=Fraction(str(num1))*Fraction(str(num2))
    result=simplify_mixed_fraction(result)
    return result

@router.get("/divide_mixed")
def divide_mixed(x: str = Query(...), y: str = Query(...)):
    res1=mixed_to_float(x)
    num1=res1["result"]
    res2=mixed_to_float(y)
    num2=res2["result"]
    result=Fraction(str(num1))/Fraction(str(num2))
    result=simplify_mixed_fraction(result)
    return result
