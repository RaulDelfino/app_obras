from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.categorias import Categoria
from app.schemas.categoria_schema import CategoriaCreate, CategoriaUpdate

def criar_categoria(db: Session, categoria: CategoriaCreate):
    existente = db.query(Categoria).filter(Categoria.nome == categoria.nome).first()
    if existente:
        raise HTTPException(status_code=400, detail="Categoria já existe")
    
    nova = Categoria(nome=categoria.nome, descricao=categoria.descricao)
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

def listar_categorias(db: Session):
    return db.query(Categoria).all()

def buscar_categoria_id(db: Session, categoria_id: int):
    categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return categoria

def atualizar_categoria(db: Session, categoria_id: int, dados: CategoriaUpdate):
    categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    
    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(categoria, campo, valor)
    
    db.commit()
    db.refresh(categoria)
    return categoria

def deletar_categoria(db: Session, categoria_id: int):
    categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    
    db.delete(categoria)
    db.commit()
    return {"mensagem": f"Categoria com ID {categoria_id} deletada com sucesso"}
