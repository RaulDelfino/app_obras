from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import SessionLocal
from app.schemas.obra_schema import ObraCreate, ObraRead, ObraUpdate
from app.crud.obra_crud import (
    criar_obra,
    listar_obras,
    buscar_obra_id,
    atualizar_obra,
    deletar_obra
)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ObraRead)
def criar(dados: ObraCreate, db: Session = Depends(get_db)):
    return criar_obra(db, dados)

@router.get("/", response_model=list[ObraRead])
def listar(db: Session = Depends(get_db)):
    return listar_obras(db)

@router.get("/{obra_id}", response_model=ObraRead)
def obter(obra_id: int, db: Session = Depends(get_db)):
    return buscar_obra_id(db, obra_id)

@router.put("/{obra_id}", response_model=ObraRead)
def editar(obra_id: int, dados: ObraUpdate, db: Session = Depends(get_db)):
    return atualizar_obra(db, obra_id, dados)

@router.delete("/{obra_id}")
def remover(obra_id: int, db: Session = Depends(get_db)):
    return deletar_obra(db, obra_id)
