from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def default_route():
    return {"Hello": "World"}
