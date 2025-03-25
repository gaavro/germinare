from fastapi import FastAPI
from app.database import Base, engine
from app.models import SoybeanMealPrice  

app = FastAPI()

Base.metadata.create_all(bind=engine) 

from app.routes import router
app.include_router(router)
