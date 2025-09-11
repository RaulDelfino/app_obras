from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import SessionLocal
from app.schemas.cliente_schema import ClienteCreate
from app.crud.cliente_crud import criar_cliente

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def cadastrar_cliente_com_usuario(dados: ClienteCreate, db: Session = Depends(get_db)):
    return criar_cliente(db, dados)
