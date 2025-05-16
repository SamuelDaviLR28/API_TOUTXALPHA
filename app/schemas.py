# app/schemas.py
from pydantic import BaseModel
from typing import List
from datetime import datetime

class PedidoCreate(BaseModel):
    cliente: str
    destino: str

class PatchBase(BaseModel):
    pedido_id: int
    valor: float
    prazo: str

class RastroBase(BaseModel):
    pedido_id: int
    status: str
    descricao: str

class MotoristaBase(BaseModel):
    pedido_id: int
    nome: str
    documento: str

class CoordenadaBase(BaseModel):
    latitude: float
    longitude: float
    timestamp: datetime

class RotaBase(BaseModel):
    pedido_id: int
    motorista_id: int
    coordenadas: List[CoordenadaBase]

class CancelamentoSuspensaoBase(BaseModel):
    pedido_id: int
    acao: str
    motivo: str
