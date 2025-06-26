from pydantic import BaseModel

class UserBase(BaseModel):
    nome: str
    email: str
    cpf: str

class LoginRequest(BaseModel):
    cpf: str
    senha: str

class UserInfoResponse(BaseModel):
    id: int
    cpf: str
    nome: str
    email: str
    
    class Config:
        orm_mode = True