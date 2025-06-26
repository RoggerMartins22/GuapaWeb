from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from services.usuario import UserService
from schemas.usuario import LoginRequest
from database.database import get_db


router = APIRouter(
    prefix="/usuario",
    tags=["users"],
)
@router.post("/login")
async def login(request_form_user: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = LoginRequest(
        cpf=request_form_user.username,
        senha=request_form_user.password
    )

    return UserService.servico_usuario_login(db=db, user=user)
