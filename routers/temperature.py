from fastapi import APIRouter,HTTPException
from pint import UnitRegistry



router=APIRouter(
    prefix='/temperature',
    tags=['temperature']

)

ureg = UnitRegistry()
Q_ = ureg.Quantity


@router.get("/")
async def convert_temperature(value: float, from_unit: str, to_unit: str):
    try:
        from_quantity = Q_(value, from_unit)
        to_quantity = from_quantity.to(to_unit)
        return {"result": round(to_quantity.magnitude,5)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
