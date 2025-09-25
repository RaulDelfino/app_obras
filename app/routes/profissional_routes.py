from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import SessionLocal
from app.schemas.profissional_schema import ProfissionalCreate, ProfissionalRead, ProfissionalUpdate
from app.crud.profissional_crud import (
    criar_profissional,
    listar_profissionais,
    buscar_profissional_id,
    atualizar_profissional,
    deletar_profissional
)

router = APIRouter()

# Dependência de sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Criar profissional + usuário
@router.post("/", response_model=ProfissionalRead)
def criar(profissional: ProfissionalCreate, db: Session = Depends(get_db)):
    return criar_profissional(db, profissional)

# Listar todos os profissionais
@router.get("/", response_model=list[ProfissionalRead])
def listar(db: Session = Depends(get_db)):
    return listar_profissionais(db)

# Buscar profissional por ID
@router.get("/{prof_id}", response_model=ProfissionalRead)
def obter(prof_id: int, db: Session = Depends(get_db)):
    return buscar_profissional_id(db, prof_id)

# Atualizar profissional
@router.put("/{prof_id}", response_model=ProfissionalRead)
def editar(prof_id: int, dados: ProfissionalUpdate, db: Session = Depends(get_db)):
    return atualizar_profissional(db, prof_id, dados)

# Deletar profissional + usuário
@router.delete("/{prof_id}")
def remover(prof_id: int, db: Session = Depends(get_db)):
    return deletar_profissional(db, prof_id)


