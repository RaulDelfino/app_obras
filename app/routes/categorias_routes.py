from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import SessionLocal
from app.schemas.categoria_schema import CategoriaCreate, CategoriaRead, CategoriaUpdate
from app.crud.categoria_crud import (
    criar_categoria,
    listar_categorias,
    buscar_categoria_id,
    atualizar_categoria,
    deletar_categoria
)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CategoriaRead)
def criar(categoria: CategoriaCreate, db: Session = Depends(get_db)):
    return criar_categoria(db, categoria)

@router.get("/", response_model=list[CategoriaRead])
def listar(db: Session = Depends(get_db)):
    return listar_categorias(db)

@router.get("/{categoria_id}", response_model=CategoriaRead)
def obter(categoria_id: int, db: Session = Depends(get_db)):
    return buscar_categoria_id(db, categoria_id)

@router.put("/{categoria_id}", response_model=CategoriaRead)
def editar(categoria_id: int, dados: CategoriaUpdate, db: Session = Depends(get_db)):
    return atualizar_categoria(db, categoria_id, dados)

@router.delete("/{categoria_id}")
def remover(categoria_id: int, db: Session = Depends(get_db)):
    return deletar_categoria(db, categoria_id)
