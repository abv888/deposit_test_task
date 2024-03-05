from decimal import Decimal

from starlette.responses import JSONResponse

from ..models.deposit import Deposit
from ..services import deposit as deposit_service
from fastapi import APIRouter, HTTPException
from pydantic import ValidationError

router = APIRouter(
    prefix="/deposit",
    tags=["deposit"],
)


@router.post("/", response_model=dict[str, float])
async def calculate_deposit(deposit_in: Deposit ) -> dict[str, float]:
        result = deposit_service.calculate_deposit(deposit_in)
        return result
