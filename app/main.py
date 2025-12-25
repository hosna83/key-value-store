from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Any
from .store import InMemoryStore, KeyNotFoundError

app = FastAPI()
store = InMemoryStore()

class KeyValue(BaseModel):
    key: str = Field(..., min_length=1, description="Key must not be empty")
    value: Any

@app.get("/")
def root():
    return {
        "message": " Welcome to Key-Value Store :)",
        "swagger": "/docs"
    }

# POST /set
@app.post("/set")
def set_key_value(item: KeyValue):
    store.set_value(item.key, item.value)
    return {"message": f"Key {item.key} set successfully."}

# GET /get/{key}
@app.get("/get/{key}")
def get_key_value(key: str):
    try:
        value = store.get_value(key)
        return {"key": key, "value": value}
    except KeyNotFoundError:
        raise HTTPException(status_code=404, detail=f"Key {key} not found")
