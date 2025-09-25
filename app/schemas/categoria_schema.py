from pydantic import BaseModel
from typing import Optional

class CategoriaBase(BaseModel):
    nome: str
    descricao: Optional[str] = None

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaUpdate(CategoriaBase):
    pass

class CategoriaRead(CategoriaBase):
    id: int

    class Config:
        from_attributes = True
