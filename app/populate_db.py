import uuid
from sqlalchemy.orm import Session
from database import SessionLocal
from app.models import SoybeanMealPrice

def populate_database():
    db: Session = SessionLocal()
    try:
        db.add_all([
            SoybeanMealPrice(id=str(uuid.uuid4()), contract_month="2023-01", price=350.50),
            SoybeanMealPrice(id=str(uuid.uuid4()), contract_month="2023-02", price=360.75),
            SoybeanMealPrice(id=str(uuid.uuid4()), contract_month="2023-03", price=370.25),
        ])
        db.commit()
        print("Banco populado com sucesso!")
    finally:
        db.close()

if __name__ == "__main__":
    populate_database()
