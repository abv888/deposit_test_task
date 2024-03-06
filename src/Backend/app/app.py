from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from .api import router

app = FastAPI(
    title='deposit calculation',
    description='This is a simple deposit calculation API',
    version='0.1',
)
app.include_router(router)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"error": " | ".join([ err['msg']  for err in exc.errors()])}))
