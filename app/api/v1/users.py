from fastapi import APIRouter, Depends

from app.api.deps import require_role


router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/admin-only")
def get_secret_data(current_user = Depends(require_role("admin"))):
    return {"message": f"Hello Admin {current_user["email"]}, here is your secret data!"}