from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import SessionLocal
from app.schemas.usuario_schema import UsuarioCreate, UsuarioRead, UsuarioUpdate
from app.crud.usuario_crud import criar_usuario, listar_usuarios, buscar_usuario_id, deletar_usuario, atualizar_usuario

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UsuarioRead)
def criar(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return criar_usuario(db, usuario)

@router.get("/", response_model=list[UsuarioRead])
def listar(db: Session = Depends(get_db)):
    return listar_usuarios(db)

@router.get("/{usuario_id}", response_model=UsuarioRead)
def obter_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = buscar_usuario_id(db,usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    else:
        return usuario
    
@router.delete("/{usuario_id}")
def remover_usuario(usuario_id: int, db: Session = Depends(get_db)):
    return deletar_usuario(db, usuario_id)

@router.put("/{usuario_id}", response_model=UsuarioRead)
def editar_usuario(usuario_id: int, dados: UsuarioUpdate, db: Session = Depends(get_db)):
    usuario_atualizado = atualizar_usuario(db, usuario_id, dados)
    return usuario_atualizado
