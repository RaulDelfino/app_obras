from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.profissional import Profissional
from app.models.usuario import Usuario, TipoUsuarioEnum
from app.schemas.profissional_schema import ProfissionalCreate, ProfissionalUpdate
from passlib.hash import bcrypt

# Criar profissional + usuário
def criar_profissional(db: Session, profissional: ProfissionalCreate):
    email_existente = db.query(Usuario).filter(Usuario.email == profissional.email).first()
    if email_existente:
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    senha_hash = bcrypt.hash(profissional.senha)
    novo_usuario = Usuario(
        nome=profissional.nome,
        email=profissional.email,
        senha_hash=senha_hash,
        tipo_usuario=TipoUsuarioEnum.profissional,
        status="ativo"
    )
    db.add(novo_usuario)
    db.flush()

    novo_profissional = Profissional(
        prof_id=novo_usuario.id,
        telefone=profissional.telefone,
        cnpj=profissional.cnpj,
        cep=profissional.cep,
        num_endereco=profissional.num_endereco,
        estrelas=profissional.estrelas
    )
    db.add(novo_profissional)
    db.commit()
    db.refresh(novo_profissional)
    return novo_profissional

# Listar todos os profissionais
def listar_profissionais(db: Session):
    return db.query(Profissional).all()

# Buscar profissional por ID
def buscar_profissional_id(db: Session, prof_id: int):
    profissional = db.query(Profissional).filter(Profissional.prof_id == prof_id).first()
    if not profissional:
        raise HTTPException(status_code=404, detail="Profissional não encontrado")
    return profissional

# Atualizar dados do profissional
def atualizar_profissional(db: Session, prof_id: int, dados: ProfissionalUpdate):
    profissional = db.query(Profissional).filter(Profissional.prof_id == prof_id).first()
    if not profissional:
        raise HTTPException(status_code=404, detail="Profissional não encontrado")
    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(profissional, campo, valor)
    db.commit()
    db.refresh(profissional)
    return profissional

# Deletar profissional + usuário vinculado
def deletar_profissional(db: Session, prof_id: int):
    profissional = db.query(Profissional).filter(Profissional.prof_id == prof_id).first()
    if not profissional:
        raise HTTPException(status_code=404, detail="Profissional não encontrado")

    usuario = db.query(Usuario).filter(Usuario.id == prof_id).first()
    if usuario:
        db.delete(usuario)
    db.delete(profissional)
    db.commit()
    return {"mensagem": f"Profissional com ID {prof_id} deletado com sucesso"}
