from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.schemas.usuario_schema import UsuarioCreate, UsuarioUpdate
from passlib.hash import bcrypt

def criar_usuario(db: Session, usuario: UsuarioCreate):
    senha_hash = bcrypt.hash(usuario.senha)
    novo_usuario = Usuario(
        nome=usuario.nome,
        email=usuario.email,
        senha_hash=senha_hash,
        telefone=usuario.telefone,
        cep=usuario.cep,
        tipo_usuario=usuario.tipo_usuario
    )
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

def listar_usuarios(db: Session):
    return db.query(Usuario).all()

def buscar_usuario_id(db: Session, usuario_id: int ):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def deletar_usuario(db: Session, usuario_id: int):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    else:
        db.delete(usuario)
        db.commit()
        return {"mensagem": f'Usuario {usuario.nome} deletado com sucesso'}
    
def atualizar_usuario(db: Session, usuario_id: int, dados: UsuarioUpdate):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(usuario,campo,valor)
    db.commit()
    db.refresh(usuario)
    return usuario
