from fastapi import Header, HTTPException, status
from app.database import SessionLocal

API_KEY = "supersecretkey2025" 

async def get_db():
    async with SessionLocal() as session:
        yield session

async def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Chave de API inválida."
        )
