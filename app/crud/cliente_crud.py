from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.models.cliente import UsuarioCliente
from app.schemas.cliente_schema import ClienteCreate
from passlib.hash import bcrypt

def criar_cliente(db: Session, dados: ClienteCreate):
    senha_hash = bcrypt.hash(dados.senha)

    novo_usuario = Usuario(
        nome=dados.nome,
        email=dados.email,
        senha_hash=senha_hash,
        telefone=dados.telefone,
        cep=dados.cep,
        tipo_usuario=dados.tipo_usuario,
        status=dados.status
    )
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    cliente = UsuarioCliente(
        usuario_id=novo_usuario.id,
        cpf=dados.cpf,
        endereco_num=dados.endereco_num,
        cep=dados.cep
    )
    db.add(cliente)
    db.commit()
    db.refresh(cliente)

    return cliente
