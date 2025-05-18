# Create hello world FastAPI app
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "It's working!"}

@app.get("/map")
def read_map():
    return {"message": "Reading the map."}

