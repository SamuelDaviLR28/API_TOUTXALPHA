from app import models, schemas
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime

async def criar_pedido(db: AsyncSession, pedido: schemas.PedidoCreate):
    db_pedido = models.Pedido(
        cliente=pedido.cliente,
        destino=pedido.destino,
        data_criacao=datetime.utcnow()
    )
    db.add(db_pedido)
    await db.commit()
    await db.refresh(db_pedido)
    return db_pedido
