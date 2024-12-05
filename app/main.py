from fastapi import FastAPI

from app.routes.users.user_routers import router as router_users

app = FastAPI()


@app.get("/")
def default_route():
    return {"say": "I'm so tired"}


app.include_router(router_users)