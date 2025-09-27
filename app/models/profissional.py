from sqlalchemy import Column, Integer, String,ForeignKey #usar atributos do SQL
from sqlalchemy.orm import relationship
from app.database.session import Base
from app.models.obra import Obra

class Profissional(Base):
    __tablename__ = "profissionais"

    prof_id = Column(Integer, ForeignKey("usuarios.id"), primary_key=True)
    telefone = Column(String(12), nullable=False)
    cnpj = Column(String(25), nullable=False)
    cep = Column(String(25), nullable=False)
    num_endereco = Column(String(5), nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)
    estrelas = Column(Integer)
    orcamento = Column(Integer, nullable=False)

    usuario = relationship("Usuario", back_populates="profissional")
    categoria = relationship("Categoria", back_populates="profissionais")
    obras = relationship("Obra", back_populates="profissional")