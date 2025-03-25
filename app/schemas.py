from pydantic import BaseModel, condecimal, root_validator
from typing import List

class PriceRequest(BaseModel):
    basis: condecimal(gt=-50, lt=50)
    contract_months: List[str]

    @root_validator(pre=True)
    def check_basis(cls, values):
        basis = values.get('basis')
        if basis is not None and not (-50 < basis < 50):
            raise ValueError("Basis must be a number between -50 and 50")
        return values

class PriceResponse(BaseModel):
    contract_month: str
    cbot_price: float
    basis: float
    flat_price: float
