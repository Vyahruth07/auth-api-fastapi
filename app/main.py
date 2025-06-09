from fastapi import FastAPI
from app.api.v1 import auth
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)  # Create database tables


def create_app() -> FastAPI:
    app= FastAPI(
        title="Authorization Server",
        version="0.1.0"
    )
    return app

    # Import and include routers here later
    # from app.api.v1 import auth
    # app.include_router(auth.router, prefix="/api/v1")

app= create_app()

app.include_router(auth.router, prefix="/api/v1")