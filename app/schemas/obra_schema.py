from pydantic import BaseModel
from typing import Optional
from datetime import date

class ObraBase(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    status: Optional[str] = "pendente"
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None
    endereco: Optional[str] = None

class ObraCreate(ObraBase):
    cliente_id: int
    profissional_id: int

class ObraUpdate(ObraBase):
    status: Optional[str] = None
    data_fim: Optional[date] = None

class ObraRead(ObraBase):
    id: int
    cliente_id: int
    profissional_id: int

    class Config:
        from_attributes = True
