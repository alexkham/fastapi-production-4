from fastapi import APIRouter
import fractions
from fractions import Fraction
from decimal import Decimal


router=APIRouter(
    prefix='/fractions',
    tags=['fractions']

)

@router.get("/to_frac/{x}/")
def frac(x):
    result=fractions.Fraction(str(x))
    return {"result":str(result)}



@router.get("/mixed/{whole_fraction}")
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
        simpl=f"{integer_part}{fraction_part}"
        simplified=simplify_mixed_fraction(result)["result"]
           
        #    # explanation.append(f"Adding {fraction1} and {fraction2}: {result}")
        return { "result": f"{result}",
                "numerator":f"{num}",
                "denominator":f"{den}",
                "simplified":f"{simpl}",
                "simplified2":f"{simplified}"}   
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
   

