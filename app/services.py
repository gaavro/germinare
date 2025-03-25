from functools import lru_cache
from sqlalchemy.orm import Session
from app.models import SoybeanMealPrice

class FlatPriceCalculator:
    CONVERSION_FACTOR = 1.10231

    @staticmethod
    def calculate(cbot_price: float, basis: float) -> float:
        return round((cbot_price + basis) * FlatPriceCalculator.CONVERSION_FACTOR, 2)

@lru_cache(maxsize=100)
def get_latest_price(session: Session, contract_month: str):
    return (
        session.query(SoybeanMealPrice.price)
        .filter(SoybeanMealPrice.contract_month == contract_month)
        .order_by(SoybeanMealPrice.created_at.desc())
        .first()
    )