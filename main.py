from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class House(BaseModel):
    adresse: str
    surface: int
    nb_rooms: int

def fake_model():
    return 1

@app.get("/")
def read_root():
    return {"Message": "API created"}

@app.post("/")
def predict_house(house: House):
    score = fake_model()
    
    return {"adresse": house.adresse,
        "prediction": score}