from contextlib import asynccontextmanager
from fastapi import FastAPI
from api.db import init_db
from api.chat.routing import router as chat_router



@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield
    
app = FastAPI(title="Docker with FastAPI", lifespan=lifespan)
app.include_router(chat_router, prefix="/chat")

@app.get("/")
def home():
    return {"message":"Home"}    

@app.get("/health")
def health(): 
    return {"status":"Healthy"}    

