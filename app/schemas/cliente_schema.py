from pydantic import BaseModel, EmailStr, constr
from datetime import datetime
from typing import Optional

# ----------- BASE -----------
class ClienteBase(BaseModel):
    telefone: str
    endereco_num: str
    cep: str
    cpf: str 


# ----------- CREATE -----------
class ClienteCreate(ClienteBase):
    # Aqui já criamos também o usuário associado
    nome: str
    email: EmailStr
    senha: str   # senha em texto plano, vai virar hash depois


# ----------- UPDATE -----------
class ClienteUpdate(BaseModel):
    telefone: Optional[str] = None
    endereco_num: Optional[str] = None
    cep: Optional[str] = None
    # cpf não costuma ser editável
    status: Optional[str] = None


# ----------- READ -----------
class ClienteRead(ClienteBase):
    cliente_id: int
    nome: str
    email: EmailStr
    data_cadastro: datetime
    status: str

    class Config:
        from_attributes = True 
