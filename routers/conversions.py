from fastapi import APIRouter, HTTPException
import pint
from pint import UnitRegistry



router=APIRouter(
    prefix='/conversions',
    tags=['conversions']

)

from fastapi import FastAPI

app = FastAPI()

@router.get("/convert/{number}")
def convert_number(number):
    number=str(number)
    # Remove common prefixes and determine the base
    base = 10  # Default to decimal
    if number.startswith("0b"):
        base = 2  # Binary
        number = number[2:]
    elif number.startswith("0x"):
        base = 16  # Hexadecimal
        number = number[2:]
    elif number.startswith("0o"):
        base = 8  # Octal
        number = number[2:]

    # Convert the input number to an integer
    try:
        num_int = int(number, base)
    except ValueError:
        return {"error": "Invalid input"}

    # Generate representations
    decimal = str(num_int)
    binary = bin(num_int)[2:]
    hexadecimal = hex(num_int)[2:]
    octal = oct(num_int)[2:]

    return {
        "decimal": decimal,
        "binary": f"0b{binary}",
        "hexadecimal": f"0x{hexadecimal}",
        "octal": f"0o{octal}"
    }

# @router.get("/convert-units/{quantity}/{from_unit}/{to_unit}")
# def convert_units(quantity,from_unit,to_unit):
#     ureg = UnitRegistry()
#     quantity=float(quantity)
#     from_unit=str(from_unit)
#     to_unit=str(to_unit)

#     try:
#         # Directly create a Quantity object
#         quantity = ureg.Quantity(quantity, str(from_unit))
#         # Perform the conversion
#         result = quantity.to(str(to_unit))
#         return result
#     except Exception as e:
#         return str(e)  # Handle any conversion errors




@router.get("/convert-units/{quantity}/{from_unit}/{to_unit}")
def convert_units(quantity: float, from_unit: str, to_unit: str):
    ureg = UnitRegistry()
    try:
        # Directly create a Quantity object
        quantity = ureg.Quantity(quantity, from_unit)
        # Perform the conversion
        result = quantity.to(to_unit)
        return {"result": str(result)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


