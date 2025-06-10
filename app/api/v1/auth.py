from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.security import verify_token
from app.schemas.user import TokenResponse, UserCreate, UserOut, UserLogin
from app.services import auth_service, user_service
from app.dependencies import get_db

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(user_service.User).filter(user_service.User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")
    new_user = user_service.create_user(db, user)
    return new_user

@router.post("/login", response_model=TokenResponse)
def login(request: UserLogin, db: Session = Depends(get_db)):
    user = auth_service.authenticate_user(request.email, request.password, db)
    return auth_service.login_user(user)

@router.post("/refresh", response_model=TokenResponse)
def refresh(refresh_token: str):
    payload = verify_token(refresh_token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
        )
    
    return {
        "access_token": auth_service.create_access_token({"sub": payload["sub"]}),
        "refresh_token": refresh_token,  # Return the same refresh token
        "token_type": "bearer"
    }
