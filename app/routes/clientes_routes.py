from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import SessionLocal
from app.schemas.cliente_schema import ClienteCreate, ClienteRead , ClienteUpdate
from app.crud.cliente_crud import (
    criar_cliente ,     
    listar_clientes,
    buscar_cliente_id,
    atualizar_cliente,
    deletar_cliente
)

router = APIRouter()

# Dependência de sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Criar cliente + usuário
@router.post("/", response_model=ClienteRead)
def criar(cliente: ClienteCreate, db: Session = Depends(get_db)):
    return criar_cliente(db, cliente)

# Listar todos os clientes
@router.get("/", response_model=list[ClienteRead])
def listar(db: Session = Depends(get_db)):
    return listar_clientes(db)

# Buscar cliente por ID
@router.get("/{cliente_id}", response_model=ClienteRead)
def obter(cliente_id: int, db: Session = Depends(get_db)):
    return buscar_cliente_id(db, cliente_id)

# Atualizar cliente
@router.put("/{cliente_id}", response_model=ClienteRead)
def editar(cliente_id: int, dados: ClienteUpdate, db: Session = Depends(get_db)):
    return atualizar_cliente(db, cliente_id, dados)

# Deletar cliente + usuário
@router.delete("/{cliente_id}")
def remover(cliente_id: int, db: Session = Depends(get_db)):
    return deletar_cliente(db, cliente_id)