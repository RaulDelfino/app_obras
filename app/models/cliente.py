from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.session import Base

class UsuarioCliente(Base):
    __tablename__ = "clientes"

    usuario_id = Column(Integer, ForeignKey("usuarios.id"), primary_key=True)
    cpf = Column(String(14), unique=True, nullable=False)
    endereco_num = Column(Integer)
    cep = Column(String(10))

    # Relacionamento com a tabela de usuários
    usuario = relationship("Usuario", back_populates="cliente")
