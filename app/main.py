from fastapi import FastAPI

from app.routers.access.access import router as access_router
from app.routers.drivers.drivers import router as drivers_router


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Let it Snow! Let it Snow! Let it Snow!"}

app.include_router(access_router)
app.include_router(drivers_router)
