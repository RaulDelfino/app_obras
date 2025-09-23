from sqlalchemy import Column, Integer, String,ForeignKey #usar atributos do SQL
from datetime import datetime
from sqlalchemy.orm import relationship
from app.database.session import Base

class Cliente(Base):
    __tablename__ = "clientes"

    cliente_id = Column(Integer, ForeignKey("usuarios.id"), primary_key=True)
    telefone = Column(String(15), nullable=False)
    endereco_num = Column(String(5), nullable=False)
    cep = Column(String(15), nullable=False)
    cpf = Column(String(14), unique=True, nullable=False)

    usuario = relationship("Usuario", back_populates="cliente")