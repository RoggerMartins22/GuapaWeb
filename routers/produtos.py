from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.produtos import ProdutoService
from schemas.produtos import ProdutoCreate, ProdutoResponse
from auth.auth import token_verifier
from database.database import get_db


router = APIRouter(
    prefix="/produtos",
    tags=["produtos"],
    dependencies=[Depends(token_verifier)]
)

@router.post("/cadastrar")
async def cadastrar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    return ProdutoService.create_produto_service(db=db, produto=produto)