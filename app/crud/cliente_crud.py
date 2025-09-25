from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.cliente import Cliente
from app.models.usuario import Usuario, TipoUsuarioEnum
from app.schemas.cliente_schema import ClienteCreate , ClienteUpdate
from passlib.hash import bcrypt

def criar_cliente(db: Session, cliente: ClienteCreate):
    # Verifica se o email já existe
    email_existente = db.query(Usuario).filter(Usuario.email == cliente.email).first()
    if email_existente:
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    # Cria o usuário
    senha_hash = bcrypt.hash(cliente.senha)
    novo_usuario = Usuario(
        nome=cliente.nome,
        email=cliente.email,
        senha_hash=senha_hash,
        tipo_usuario=TipoUsuarioEnum.cliente,
        status="ativo"
    )
    db.add(novo_usuario)
    db.flush()  # Garante que novo_usuario.id esteja disponível antes de usar

    # Cria o cliente vinculado ao usuário
    novo_cliente = Cliente(
        cliente_id=novo_usuario.id,
        telefone=cliente.telefone,
        cpf=cliente.cpf,
        cep=cliente.cep,
        num_endereco=cliente.num_endereco,
        estrelas=cliente.estrelas
    )
    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)
    return novo_cliente

# Listar todos os clientes
def listar_clientes(db: Session):
    return db.query(Cliente).all()

# Buscar cliente por ID
def buscar_cliente_id(db: Session, cliente_id: int):
    cliente = db.query(Cliente).filter(Cliente.cliente_id == cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente

# Atualizar dados do cliente
def atualizar_cliente(db: Session, cliente_id: int, dados: ClienteUpdate):
    cliente = db.query(Cliente).filter(Cliente.cliente_id == cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    
    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(cliente, campo, valor)
    
    db.commit()
    db.refresh(cliente)
    return cliente

# Deletar cliente e usuário vinculado
def deletar_cliente(db: Session, cliente_id: int):
    cliente = db.query(Cliente).filter(Cliente.cliente_id == cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    
    usuario = db.query(Usuario).filter(Usuario.id == cliente_id).first()
    if usuario:
        db.delete(usuario)
    
    db.delete(cliente)
    db.commit()
    return {"mensagem": f"Cliente com ID {cliente_id} deletado com sucesso"}


