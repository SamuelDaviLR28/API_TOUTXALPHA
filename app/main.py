import os
import asyncio
from fastapi import FastAPI, Depends, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from app.dependencies import get_db, verify_api_key
from app import crud, schemas
from app.database import engine, Base
import os

print("DATABASE_URL:", os.getenv("DATABASE_URL"))

app = FastAPI(title="API Transportadora Parceira")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def processar_pedido(db: AsyncSession, pedido: schemas.PedidoCreate):
    await crud.criar_pedido(db, pedido)
    await asyncio.sleep(300)  # Simula delay ou tempo de processamento

@app.post("/dispatch", dependencies=[Depends(verify_api_key)])
async def post_dispatch(
    pedido: schemas.PedidoCreate,
    db: AsyncSession = Depends(get_db),
    background_tasks: BackgroundTasks  # sem Depends()
):
    background_tasks.add_task(processar_pedido, db, pedido)
    return {"message": "Pedido recebido e será processado em segundo plano."}
