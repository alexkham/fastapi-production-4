from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import routers
from routers import basic,logarithms,trigonometry,aggregate,fractions,roots,constants,groups,conversions




app = FastAPI()
app.include_router(routers.basic.router)
app.include_router(routers.logarithms.router)
app.include_router(routers.trigonometry.router)
app.include_router(routers.aggregate.router)
app.include_router(routers.fractions.router)
app.include_router(routers.roots.router)
app.include_router(routers.constants.router)
app.include_router(routers.groups.router)
app.include_router(routers.conversions.router)




origins = ["http://localhost:3000"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Fourth Project ,Please"}

@app.get("/ask")
async def ask():
    return {"message": "How are  you today Ah You??"}

