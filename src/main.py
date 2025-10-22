
from fastapi import FastAPI
from src.container import MainContainer

app = FastAPI()
main_container = MainContainer()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.container = main_container