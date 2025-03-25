from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas import PriceRequest, PriceResponse
from app.database import get_db
from app.services import FlatPriceCalculator, get_latest_price
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

router = APIRouter()

@router.post("/api/flat_price", response_model=dict)
def calculate_flat_price(request: PriceRequest, db: Session = Depends(get_db)):
    results = []
    
    try:
        for contract_month in request.contract_months:
            latest_price = get_latest_price(db, contract_month)
            
            if not latest_price:
                raise HTTPException(status_code=404, detail=f"Contract month {contract_month} not found")
            
            cbot_price = float(latest_price[0])
            flat_price = FlatPriceCalculator.calculate(cbot_price, float(request.basis))
            
            results.append(PriceResponse(
                contract_month=contract_month,
                cbot_price=cbot_price,
                basis=float(request.basis),
                flat_price=flat_price
            ).dict())
        
        return {"results": results}
    
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="An unexpected error occurred on the server")
