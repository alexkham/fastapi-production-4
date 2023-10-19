from fastapi import FastAPI
import routers
from routers import basic,logarithms,trigonometry,aggregate,fractions,roots,constants




app = FastAPI()
app.include_router(routers.basic.router)
app.include_router(routers.logarithms.router)
app.include_router(routers.trigonometry.router)
app.include_router(routers.aggregate.router)
app.include_router(routers.fractions.router)
app.include_router(routers.roots.router)
app.include_router(routers.constants.router)


@app.get("/")
async def root():
    return {"message": "Fourth Project ,Please"}

@app.get("/ask")
async def ask():
    return {"message": "How are  you today Ah You??"}

