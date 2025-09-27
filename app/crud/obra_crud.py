from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.obra import Obra
from app.schemas.obra_schema import ObraCreate, ObraUpdate

# Criar obra
def criar_obra(db: Session, dados: ObraCreate):
    nova_obra = Obra(**dados.model_dump())
    db.add(nova_obra)
    db.commit()
    db.refresh(nova_obra)
    return nova_obra

# Listar todas as obras
def listar_obras(db: Session):
    return db.query(Obra).all()

# Buscar obra por ID
def buscar_obra_id(db: Session, obra_id: int):
    obra = db.query(Obra).filter(Obra.id == obra_id).first()
    if not obra:
        raise HTTPException(status_code=404, detail="Obra não encontrada")
    return obra

# Atualizar obra
def atualizar_obra(db: Session, obra_id: int, dados: ObraUpdate):
    obra = db.query(Obra).filter(Obra.id == obra_id).first()
    if not obra:
        raise HTTPException(status_code=404, detail="Obra não encontrada")
    
    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(obra, campo, valor)
    
    db.commit()
    db.refresh(obra)
    return obra

# Deletar obra
def deletar_obra(db: Session, obra_id: int):
    obra = db.query(Obra).filter(Obra.id == obra_id).first()
    if not obra:
        raise HTTPException(status_code=404, detail="Obra não encontrada")
    
    db.delete(obra)
    db.commit()
    return {"mensagem": f"Obra com ID {obra_id} deletada com sucesso"}
