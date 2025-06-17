from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.security import OAuth2PasswordBearer
from app.api.v1 import auth, users
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)  # Create database tables


def create_app() -> FastAPI:
    app= FastAPI(
        title="Authorization Server",
        version="0.1.0"
    )

    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    app.include_router(auth.router, prefix="/api/v1")
    app.include_router(users.router, prefix="/api/v1")

    def custom_openapi():
        if app.openapi_schema:
            return app.openapi_schema
        openapi_schema = get_openapi(
            title=app.title,
            version=app.version,
            description="Auth API with JWT",
            routes=app.routes,
        )
                    
        app.openapi_schema = openapi_schema
        return app.openapi_schema

    app.openapi = custom_openapi
    return app

    # Import and include routers here later
    # from app.api.v1 import auth
    # app.include_router(auth.router, prefix="/api/v1")

app= create_app()