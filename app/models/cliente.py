from sqlalchemy import Column, Integer, String,ForeignKey #usar atributos do SQL
from sqlalchemy.orm import relationship
from app.database.session import Base

class Cliente(Base):
    __tablename__ = "clientes"

    cliente_id = Column(Integer, ForeignKey("usuarios.id"), primary_key=True)
    telefone = Column(String(12), nullable=False)
    cpf = Column(String(25), nullable=False)
    cep = Column(String(25), nullable=False)
    num_endereco = Column(String(5), nullable=False)
    estrelas = Column(Integer)

    usuario = relationship("Usuario", back_populates="cliente")
