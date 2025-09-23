from sqlalchemy import Column, Integer, String, DateTime, Enum #usar atributos do SQL
from datetime import datetime
from app.database.session import Base
from sqlalchemy.orm import relationship
import enum

class TipoUsuarioEnum(str, enum.Enum):
    cliente = "cliente"
    profissional = "profissional"

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    senha_hash = Column(String(255), nullable=False)
    tipo_usuario = Column(Enum(TipoUsuarioEnum), nullable=False)
    data_cadastro = Column(DateTime, default=datetime.utcnow)
    status = Column(String(20), default="ativo")    
    #cliente = relationship("UsuarioCliente", back_populates="usuario", uselist=False)