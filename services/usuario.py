from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from repository.usuario import UserRepository
from auth.hashing import AuthHandler
from auth.auth import OAuth2
from schemas.usuario import LoginRequest

class UserService:

    @staticmethod            
    def servico_usuario_login(db: Session, user: LoginRequest):
        user_db = UserRepository.consulta_usuario_por_cpf(db=db, cpf=user.cpf)

        if not user_db:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Usuário não encontrado"
            )
        
        elif not AuthHandler.verify_password(user.senha, user_db.senha):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="CPF ou senha incorreta!"
            )
        
        return OAuth2.user_login(user_db)