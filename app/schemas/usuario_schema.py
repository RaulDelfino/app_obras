from pydantic import BaseModel, EmailStr
from enum import Enum
from typing import Optional

#criação de classe que seram usadas nos cruds

# classe para identificar o tipo do usuario
class TipoUsuarioEnum(str, Enum):
    cliente = "cliente"
    profissional = "profissional"

# classe para o usuario base
class UsuarioBase(BaseModel):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    tipo_usuario: Optional[TipoUsuarioEnum] = None

#Classe de criação que obriga a inserção dos campos
class UsuarioCreate(UsuarioBase):
    nome: str
    email: EmailStr
    tipo_usuario: TipoUsuarioEnum
    senha: str

# classe que vai mostrar os atributos dos usuarios - sem senha 
class UsuarioRead(UsuarioBase):
    id: int
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    tipo_usuario: Optional[TipoUsuarioEnum] = None
    status: Optional[str] = None

    class Config:
        orm_mode = True

# classe de update do usuario
class UsuarioUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    tipo_usuario: Optional[TipoUsuarioEnum]= None
    status: Optional[str]= None

    class Config:
        orm_mode = True
