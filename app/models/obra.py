from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database.session import Base

class Obra(Base):
    __tablename__ = "obras"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), nullable=False)
    descricao = Column(String(255), nullable=True)
    status = Column(String(20), default="pendente")
    data_inicio = Column(Date, nullable=True)
    data_fim = Column(Date, nullable=True)
    endereco = Column(String(150), nullable=True)

    cliente_id = Column(Integer, ForeignKey("clientes.cliente_id"), nullable=False)
    profissional_id = Column(Integer, ForeignKey("profissionais.prof_id"), nullable=False)

    cliente = relationship("Cliente", back_populates="obras")
    profissional = relationship("Profissional", back_populates="obras")
