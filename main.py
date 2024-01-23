from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import routers
from routers import octal,hexadecimal,binary,basic,logarithms,trigonometry,aggregate,fractions,roots,constants,groups,conversions,temperature




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
app.include_router(routers.binary.router)
app.include_router(routers.hexadecimal.router)
app.include_router(routers.octal.router)
app.include_router(routers.temperature.router)




origins = ["http://localhost:3001","167.248.133.188","https://www.calculateonline.net",
           "http://localhost:3000",  
    "http://127.0.0.1:3000"]


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


@app.get("/api/your-content")
async def get_content():
    # Handle data generation and return in desired format (JSON, HTML, etc.)
    return {"message": "Hello from FastAPI! /n x+y=z"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
