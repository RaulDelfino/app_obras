import bcrypt
from sqlalchemy.orm import Session
from app.models.usuario import Usuario, TipoUsuarioEnum
from app.models.cliente import Cliente
from app.schemas.cliente_schema import ClienteCreate, ClienteUpdate

# Função de hash usando bcrypt
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# ---------- CREATE ----------
def create_cliente(db: Session, cliente_in: ClienteCreate) -> Cliente:
    # 1. Criar o Usuario
    usuario = Usuario(
        nome=cliente_in.nome,
        email=cliente_in.email,
        senha_hash=hash_password(cliente_in.senha),
        tipo_usuario=TipoUsuarioEnum.cliente
    )
    db.add(usuario)
    db.flush()  # garante que o ID do usuário seja gerado antes do cliente

    # 2. Criar o Cliente associado
    cliente = Cliente(
        cliente_id=usuario.id,
        telefone=cliente_in.telefone,
        endereco_num=cliente_in.endereco_num,
        cep=cliente_in.cep,
        cpf=cliente_in.cpf,
        usuario=usuario
    )
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente


# ---------- READ ----------
def get_cliente(db: Session, cliente_id: int) -> Cliente | None:
    return db.query(Cliente).filter(Cliente.cliente_id == cliente_id).first()


def get_clientes(db: Session, skip: int = 0, limit: int = 100) -> list[Cliente]:
    return db.query(Cliente).offset(skip).limit(limit).all()


# ---------- UPDATE ----------
def update_cliente(db: Session, cliente_id: int, cliente_in: ClienteUpdate) -> Cliente | None:
    cliente = db.query(Cliente).filter(Cliente.cliente_id == cliente_id).first()
    if not cliente:
        return None

    update_data = cliente_in.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(cliente, key, value)

    db.commit()
    db.refresh(cliente)
    return cliente


# ---------- DELETE (opcional) ----------
def delete_cliente(db: Session, cliente_id: int) -> bool:
    cliente = db.query(Cliente).filter(Cliente.cliente_id == cliente_id).first()
    if not cliente:
        return False
    db.delete(cliente)
    db.commit()
    return True
