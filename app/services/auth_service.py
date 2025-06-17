from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.core.security import create_access_token, create_refresh_token
from app.models import user as models
from app.utils.password import verify_password

def authenticate_user(email: str, password: str, db: Session):
    """Authenticate a user by email and password."""
    db_user = db.query(models.User).filter(models.User.email == email).first()
    if not db_user or not verify_password(password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return db_user

def login_user(user: models.User):
    token_data = {"sub" : user.email, "role": user.role}
    access_token = create_access_token(token_data)
    refresh_token = create_refresh_token(token_data)  # No expiration for refresh token

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }