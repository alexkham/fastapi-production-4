from fastapi import APIRouter, Query
import math
import fractions
import numpy as np
from enum import Enum
INFINITY_THRESHOLD = 1e15
FLOATING_POINT_THRESHOLD = 1e-10

router=APIRouter(
    prefix='/trigo',
    tags=['trigonometry']

)


# def convert_angle(x: float, unit: str) -> float:
    
#     return x if unit == 'radians' else np.radians(x)

# @router.get("/sin/{x}/{unit}/")
# def get_sin(x: float, unit: str ):
#     x = convert_angle(x, unit)
#     result = np.sin(x)
#     result = np.round(result, 5)
#     return {"result": str(result)}

# # Repeat the same for other trigonometric functions
# @router.get("/csc/{x}/")
# def get_csc(x: float, unit: str = Query('degrees', enum=['degrees', 'radians'])):
#     x = convert_angle(x, unit)
#     result = 1 / np.sin(x)
#     result = np.round(result, 5)
#     return {"result": str(result)}





# @router.get("/radians/{x}/")
# def get_radians(x):
#     result=math.radians(float(x))
#     result=round(result,5)
#     return {"result":str(result)}




# @router.get("/sin/{x}/")
# def get_sin(x: float):
#     result = np.sin(np.radians(x))
#     result = np.round(result, 5)
#     return {"result": str(result)}

# def convert_angle(x: float, unit: str) -> float:
#     """Converts the angle to radians if it's in degrees."""
#     return x if unit == 'radians' else np.radians(x)


class Unit(str, Enum):
    degrees = "degrees"
    radians = "radians"

@router.get("/sin/{x}/")
def get_sin(x: float, unit: Unit= Unit.degrees):
    x = x if unit == Unit.radians else np.radians(x)
    result = np.sin(x)    
    result = np.round(result, 5)
    return {"result": str(result)}

@router.get("/cos/{x}/")
def get_cos(x: float, unit: Unit= Unit.degrees):
    x = x if unit == Unit.radians else np.radians(x)
    result = np.cos(x)
    result = np.round(result, 5)
    return {"result": str(result)}

@router.get("/tan/{x}/")
def get_tan(x: float, unit: Unit= Unit.degrees):
    x = x if unit == Unit.radians else np.radians(x)
    result = np.tan(x)
    result = np.round(result, 5)
    return {"result": str(result)}

@router.get("/csc/{x}/")
def get_csc(x: float, unit: Unit= Unit.degrees):
    x = x if unit == Unit.radians else np.radians(x)
    result = 1 / np.sin(x)
    result = np.round(result, 5)
    return {"result": str(result)}

@router.get("/sec/{x}/")
def get_sec(x: float, unit: Unit= Unit.degrees):
    x = x if unit == Unit.radians else np.radians(x)
    result = 1 / np.cos(x)
    result = np.round(result, 5)
    return {"result": str(result)}

@router.get("/cot/{x}/")
def get_cot(x: float, unit: Unit= Unit.degrees):
    x = x if unit == Unit.radians else np.radians(x)
    result = 1 / np.tan(x)
    result = np.round(result, 5)
    return {"result": str(result)}


def handle_infinity(value):
    """Returns None if the value exceeds the threshold for infinity."""
    # if abs(value) > INFINITY_THRESHOLD:
    #     return None  # This is JSON-compliant and can be interpreted as 'undefined' or 'infinity'
    if abs(value)<FLOATING_POINT_THRESHOLD:
        return float(0)
    else:
        return np.round(value, 5)
    
def normalize_angle(x: float, unit: Unit):
    """Normalize the angle to the range [0, 2π) and converts to radians if needed."""
    if unit == Unit.degrees:
        x = x % 360
        x = np.radians(x)  # Convert to radians
    else:  # Radians
        x = x % (2 * np.pi)
    return x
@router.get("/all_trigo/{x}/")
def get_all_trigo_values(x: float, unit: Unit = Query(default=Unit.degrees)):
    x = normalize_angle(x, unit)
    sin_val = np.sin(x)
    cos_val = np.cos(x)

    # Manually set sin_val and cos_val to 0 if they're within the threshold of zero
    if abs(sin_val) < FLOATING_POINT_THRESHOLD:
        sin_val = 0.0
    if abs(cos_val) < FLOATING_POINT_THRESHOLD:
        cos_val = 0.0
    # if abs(tan_val) < FLOATING_POINT_THRESHOLD:
    #     tan_val = 0.0
    # if abs(cot_val) < FLOATING_POINT_THRESHOLD:
    #     cot_val = 0.0
    # if abs(csc_val) < FLOATING_POINT_THRESHOLD:
    #     csc_val = 0.0
    # if abs(sec_val) < FLOATING_POINT_THRESHOLD:
    #     sec_val = 0.0

    # Directly check if sin_val or cos_val are zero
    tan_val = None if cos_val == 0 else sin_val/cos_val
    cot_val = None if sin_val == 0 else 1 / sin_val

    csc_val = None if sin_val == 0 else 1 / sin_val
    sec_val = None if cos_val == 0 else 1 / cos_val

    result = {
        "sin": sin_val,
        "cos": cos_val,
        "tan": tan_val,
        "csc": csc_val,
        "sec": sec_val,
        "cot": cot_val
    }
    return result


# @router.get("/all_trigo/{x}/")
# def get_all_trigo_values(x: float, unit: Unit = Query(default=Unit.degrees)):
#     x = normalize_angle(x, unit)
#     sin_val = handle_infinity(np.sin(x))
#     cos_val = handle_infinity(np.cos(x))

#     # Manually set sin_val and cos_val to 0 if they're within the threshold of zero
#     # if abs(sin_val) < FLOATING_POINT_THRESHOLD:
#     #     sin_val = float(0)
#     # if abs(cos_val) < FLOATING_POINT_THRESHOLD:
#     #     cos_val = float(0)

#     tan_val = None if abs(cos_val) < FLOATING_POINT_THRESHOLD else np.tan(x)
#     cot_val = None if abs(sin_val) < FLOATING_POINT_THRESHOLD else 1 / sin_val

#     csc_val = None if abs(sin_val) < FLOATING_POINT_THRESHOLD else 1 / sin_val
#     sec_val = None if abs(cos_val) < FLOATING_POINT_THRESHOLD else 1 / cos_val

#     result = {
#         "sin": handle_infinity(sin_val),
#         "cos": handle_infinity(cos_val),
#         "tan": handle_infinity(tan_val),
#         "csc": handle_infinity(csc_val),
#         "sec": handle_infinity(sec_val),
#         "cot": handle_infinity(cot_val)
#     }
#     return result

# @router.get("/all_trigo/{x}/")
# def get_all_trigo_values(x: float, unit: Unit = Query(default=Unit.degrees)):
#     x = normalize_angle(x, unit)
#     sin_val = np.sin(x)
#     cos_val = np.cos(x)

#     # Check if values are close enough to zero to be considered as zero
#     tan_val = None if abs(cos_val) < FLOATING_POINT_THRESHOLD else np.tan(x)
#     cot_val = None if abs(sin_val) < FLOATING_POINT_THRESHOLD else 1 / sin_val

#     csc_val = None if abs(sin_val) < FLOATING_POINT_THRESHOLD else 1 / sin_val
#     sec_val = None if abs(cos_val) < FLOATING_POINT_THRESHOLD else 1 / cos_val

#     result = {
#         "sin": sin_val,
#         "cos": cos_val,
#         "tan": tan_val,
#         "csc": csc_val,
#         "sec": sec_val,
#         "cot": cot_val
#     }
#     return result

# @router.get("/all_trigo/{x}/")
# def get_all_trigo_values(x: float, unit: Unit = Query(default=Unit.degrees)):
#     x = normalize_angle(x, unit)
#     sin_val = np.sin(x)
#     cos_val = np.cos(x)

#     # Simple checks for undefined conditions
#     tan_val = None if cos_val == 0 else np.tan(x)
#     cot_val = None if sin_val == 0 else 1 / sin_val

#     csc_val = None if sin_val == 0 else 1 / sin_val
#     sec_val = None if cos_val == 0 else 1 / cos_val

#     result = {
#         "sin": sin_val,
#         "cos": cos_val,
#         "tan": tan_val,
#         "csc": csc_val,
#         "sec": sec_val,
#         "cot": cot_val
#     }
#     return result


# @router.get("/all_trigo/{x}/")
# def get_all_trigo_values(x: float, unit: Unit = Query(default=Unit.degrees)):
#     x = normalize_angle(x, unit)
#     sin_val = np.sin(x)
#     cos_val = np.cos(x)

#     # Handle special cases for tan, csc, sec, and cot
#     if cos_val == 0:  # When cosine is zero, tan is undefined
#         tan_val = None
#     else:
#         tan_val = handle_infinity(np.tan(x))

#     csc_val = None if sin_val == 0 else handle_infinity(1 / sin_val)
#     sec_val = None if cos_val == 0 else handle_infinity(1 / cos_val)
#     cot_val = None if tan_val in [0, None] else handle_infinity(cos_val/sin_val)

#     result = {
#         "sin":sin_val,
#         "cos":cos_val,
#         "tan": tan_val,
#         "csc": csc_val,
#         "sec": sec_val,
#         "cot": cot_val
#     }
#     return result



# def handle_infinity(value):
#     """Returns 'undefined' if the value exceeds the threshold for infinity. 
#     Zero values are considered valid and are returned as is."""
#     if abs(value) > INFINITY_THRESHOLD:
#         return 'undefined'
#     else:
#         return np.round(value, 5)

# def normalize_angle(x: float, unit: Unit):
#     """Normalize the angle to the range [0, 2π) and converts to radians if needed."""
#     if unit == Unit.degrees:
#         x = x % 360
#         x = np.radians(x)  # Convert to radians
#     else:  # Radians
#         x = x % (2 * np.pi)
#     return x
# def handle_infinity(value):
#     """Returns a JSON-compliant representation of the value."""
#     if np.isinf(value) or np.isnan(value):
#         return str(value)
#     else:
#         return np.round(value, 5)

# def normalize_angle(x: float, unit: Unit):
#     """Normalize the angle to the range [0, 2π) and converts to radians if needed."""
#     if unit == Unit.degrees:
#         x = x % 360
#         x = np.radians(x)  # Convert to radians
#     else:  # Radians
#         x = x % (2 * np.pi)
#     return x

# @router.get("/all_trigo/{x}/")
# def get_all_trigo_values(x: float, unit: Unit = Unit.degrees):
#     x = normalize_angle(x, unit)
#     sin_val = np.sin(x)
#     cos_val = np.cos(x)
#     tan_val = np.tan(x)
#     csc_val = 'undefined' if sin_val == 0 else 1 / sin_val
#     sec_val = 'undefined' if cos_val == 0 else 1 / cos_val
#     cot_val = 'undefined' if tan_val == 0 else 1 / tan_val

#     result = {
#         "sin": handle_infinity(sin_val),
#         "cos": handle_infinity(cos_val),
#         "tan": handle_infinity(tan_val),
#         "csc": handle_infinity(csc_val),
#         "sec": handle_infinity(sec_val),
#         "cot": handle_infinity(cot_val)
#     }
#     return result

# @router.get("/all_trigo/{x}/")
# def get_all_trigo_values(x: float, unit: Unit = Query(default=Unit.degrees)):
#     x = normalize_angle(x, unit)
#     sin_val = np.sin(x)
#     cos_val = np.cos(x)
#     tan_val = None  if cos_val == 0 else sin_val/ cos_val
#     csc_val = None  if sin_val == 0 else 1 / sin_val
#     sec_val = None if cos_val == 0 else 1 / cos_val
#     cot_val = None if sin_val == 0 else cos_val/sin_val

#     result = {
#         "sin": np.round(sin_val,5),
#         "cos": np.round(cos_val,5),
#         "tan": np.round(tan_val,5),
#         "csc": np.round(csc_val,5),
#         "sec": np.round(sec_val,5),
#         "cot": np.round(cot_val,5)
#     }
#     return result



# @router.get("/all_trigo/{x}/")
# def get_all_trigo_values(x: float, unit: Unit = Unit.degrees):
#     x = x if unit == Unit.radians else np.radians(x)
#     sin_val = np.sin(x)
#     cos_val = np.cos(x)
#     tan_val = np.tan(x)
#     csc_val = 1 / sin_val if sin_val != 0 else float('inf')
#     sec_val = 1 / cos_val if cos_val != 0 else float('inf')
#     cot_val = 1 / tan_val if tan_val != 0 else float('inf')

#     result = {
#         "sin": np.round(sin_val, 5),
#         "cos": np.round(cos_val, 5),
#         "tan": np.round(tan_val, 5),
#         "csc": np.round(csc_val, 5),
#         "sec": np.round(sec_val, 5),
#         "cot": np.round(cot_val, 5)
#     }
#     return result



# @router.get("/csc/{x}/")
# def get_csc(x: float):
#     result = 1 / np.sin(np.radians(x))
#     result = np.round(result, 5)
#     return {"result": str(result)}

# @router.get("/cos/{x}/")
# def get_cos(x: float):
#     result = np.cos(np.radians(x))
#     result = np.round(result, 5)
#     return {"result": str(result)}

# @router.get("/sec/{x}/")
# def get_sec(x: float):
#     result = 1 / np.cos(np.radians(x))
#     result = np.round(result, 5)
#     return {"result": str(result)}

# @router.get("/tan/{x}/")
# def get_tan(x: float):
#     result = np.tan(np.radians(x))
#     result = np.round(result, 5)
#     return {"result": str(result)}

# @router.get("/cot/{x}/")
# def get_cot(x: float):
#     result = 1 / np.tan(np.radians(x))
#     result = np.round(result, 5)
#     return {"result": str(result)}




# @router.get("/sin/{x}/")
# def get_sin(x):
#     x=float(x)
#     result=math.sin(math.radians(x))
#     result=round(result,5)
#     return {"result":str(result)}

# def round_to_multiple(number, multiple):
#     return multiple * round(number / multiple)

# @router.get("/csc/{x}/")
# def get_csc(x):
#     x=float(x)
#     result=1/(math.sin(math.radians(x)))
#     result=round(result,5)
#     return {"result":str(result)}


# @router.get("/cos/{x}/")
# def get_cos(x):
#     x=float(x)
#     result=math.cos(math.radians(x))
#     result=round(result,5)
#     return {"result":str(result)}

# @router.get("/sec/{x}/")
# def get_sec(x):
#     x=float(x)
#     result=1/(math.cos(math.radians(x)))
#     result=round(result,5)
#     return {"result":str(result)}

# @router.get("/tan/{x}/")
# def get_tan(x):
#     x=float(x)
#     result=math.tan(math.radians(x))
#     result=round(result,5)
#     return {"result":str(result)}

# @router.get("/cot/{x}/")
# def get_cot(x):
#     x=float(x)
#     result=1/(math.tan(math.radians(x)))
#     result=round(result,5)
#     return {"result":str(result)}