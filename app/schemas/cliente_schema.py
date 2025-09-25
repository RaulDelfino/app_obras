from pydantic import BaseModel, EmailStr, constr
from datetime import datetime
from typing import Optional
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
class ClienteBase(BaseModel):
    telefone: Optional[str] = None
    cpf: Optional[str] = None
    cep: Optional[str] = None
    num_endereco: Optional[str] = None
    estrelas: Optional[int] = None

# ----------- CREATE -----------
class ClienteCreate(ClienteBase):
    nome: str
    email: EmailStr
    senha: str
    telefone: str
    cpf: str
    cep: str
    num_endereco: str
    estrelas: Optional[int] = None

# ----------- UPDATE -----------
class ClienteUpdate(BaseModel):
    telefone: Optional[str] = None
    cpf: Optional[str] = None
    cep: Optional[str] = None
    num_endereco: Optional[str] = None
    estrelas: Optional[int] = None

    class Config:
        from_attributes = True

# ----------- READ -----------
class ClienteRead(ClienteBase):
    cliente_id: int
    usuario: UsuarioEmbedded  # Dados do usuário vinculados

    class Config:
        from_attributes = True
