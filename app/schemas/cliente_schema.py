from pydantic import BaseModel, EmailStr
from typing import Optional
from app.models.usuario import TipoUsuarioEnum

class ClienteCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    telefone: Optional[str]
    cep: Optional[str]
    cpf: str
    endereco_num: Optional[int]
    tipo_usuario: TipoUsuarioEnum = TipoUsuarioEnum.cliente  # fixo como cliente
    status: Optional[str] = "ativo"
