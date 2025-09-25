from fastapi import FastAPI
from app.database.session import Base, engine
from app.routes import usuario_routes, clientes_routes, profissional_routes, categorias_routes
# uvicorn app.main:app --reload          ------- para rodar o codigo
app = FastAPI(title="API do TCC")

# Importar rotas aqui depois
# from app.api import usuario_routes, obra_routes, categoria_routes


app.include_router(usuario_routes.router, prefix="/usuarios", tags=["Usuários"])
app.include_router(clientes_routes.router, prefix="/clientes", tags=["clientes"])
app.include_router(profissional_routes.router, prefix="/profissionais", tags=["Profissionais"])
app.include_router(categorias_routes.router, prefix="/categorias", tags=["Categorias"]) 

# app.include_router(usuario_routes.router)

# Criar tabelas no banco
Base.metadata.create_all(bind=engine)