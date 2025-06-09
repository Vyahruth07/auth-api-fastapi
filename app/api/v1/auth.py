from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut
from app.services import user_service
from app.dependencies import get_db

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(user_service.User).filter(user_service.User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")
    new_user = user_service.create_user(db, user)
    return new_user