from fastapi import FastAPI
from config.database import engine, Base
from controllers import user_controller, ticket_controller
# Este proyecto esta construido con arquitectura MVCS (model view(routes) controller schemas)
app = FastAPI()

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Registrar los controladores (routers)
app.include_router(user_controller.router)
app.include_router(ticket_controller.router)
