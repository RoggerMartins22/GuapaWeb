from pydantic import BaseModel
from typing import List, Optional

class ProdutoCreate(BaseModel):
    nome: str
    descricao: Optional[str] = ""
    preco: float
    tamanhos: List[str]

class ProdutoResponse(BaseModel):
    id: int
    nome: str
    descricao: Optional[str] = ""
    preco: float
    tamanhos: List[str]

    class Config:
        orm_mode = True
