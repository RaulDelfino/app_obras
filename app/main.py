from fastapi import FastAPI
from app.database.session import Base, engine
from app.routes import usuario_routes, clientes_routes
# uvicorn app.main:app --reload          ------- para rodar o codigo
app = FastAPI(title="API do TCC")

# Importar rotas aqui depois
# from app.api import usuario_routes, obra_routes, categoria_routes


app.include_router(usuario_routes.router, prefix="/usuarios", tags=["Usuários"])
app.include_router(clientes_routes.router, prefix="/clentes", tags=["Clientes"])

# app.include_router(usuario_routes.router)

# Criar tabelas no banco
Base.metadata.create_all(bind=engine)