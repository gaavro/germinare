from sqlalchemy import Column, String, DECIMAL, TIMESTAMP, func
from app.database import Base

class SoybeanMealPrice(Base):
    __tablename__ = "soybean_meal_prices"
    
    id = Column(String, primary_key=True)
    contract_month = Column(String, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())