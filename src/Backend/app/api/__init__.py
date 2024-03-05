from fastapi import APIRouter
from .deposit_calculator import router as deposit

router = APIRouter()
router.include_router(deposit)
