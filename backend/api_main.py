from contextlib import asynccontextmanager
from fastapi import FastAPI
from api.db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield
    
app = FastAPI(title="Docker with FastAPI", lifespan=lifespan)

@app.get("/")
def home():
    return {"message":"Home"}    

@app.get("/health")
def health(): 
    return {"status":"Healthy"}    

