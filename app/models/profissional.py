from sqlalchemy import Column, Integer, String,ForeignKey #usar atributos do SQL
from sqlalchemy.orm import relationship
from app.database.session import Base

class Profissional(Base):
    __tablename__ = "profissionais"

    prof_id = Column(Integer, ForeignKey("usuarios.id"), primary_key=True)
    telefone = Column(String(12), nullable=False)
    cnpj = Column(String(25), nullable=False)
    cep = Column(String(25), nullable=False)
    num_endereco = Column(String(5), nullable=False)
    estrelas = Column(Integer)

    usuario = relationship("Usuario", back_populates="profissional")