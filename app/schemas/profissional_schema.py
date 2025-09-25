from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from enum import Enum

# Enum para tipo de usuário
class TipoUsuarioEnum(str, Enum):
    cliente = "cliente"
    profissional = "profissional"

# ----------- USUÁRIO EMBUTIDO -----------
class UsuarioEmbedded(BaseModel):
    id: int
    nome: str
    email: EmailStr
    senha_hash: str
    tipo_usuario: TipoUsuarioEnum
    data_cadastro: Optional[datetime]
    status: str

    class Config:
        from_attributes = True

# ----------- BASE -----------
class ProfissionalBase(BaseModel):
    telefone: Optional[str] = None
    cnpj: Optional[str] = None
    cep: Optional[str] = None
    num_endereco: Optional[str] = None
    estrelas: Optional[int] = None

# ----------- CREATE -----------
class ProfissionalCreate(ProfissionalBase):
    nome: str
    email: EmailStr
    senha: str
    telefone: str
    cnpj: str
    cep: str
    num_endereco: str
    estrelas: Optional[int] = None

# ----------- UPDATE -----------
class ProfissionalUpdate(BaseModel):
    telefone: Optional[str] = None
    cnpj: Optional[str] = None
    cep: Optional[str] = None
    num_endereco: Optional[str] = None
    estrelas: Optional[int] = None

    class Config:
        from_attributes = True

# ----------- READ -----------
class ProfissionalRead(ProfissionalBase):
    prof_id: int
    usuario: UsuarioEmbedded

    class Config:
        from_attributes = True
