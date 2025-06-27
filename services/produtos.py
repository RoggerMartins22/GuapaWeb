from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from schemas.produtos import ProdutoCreate
from repository.produtos import ProdutoRepository  

class ProdutoService:

    @staticmethod
    def create_produto_service(db: Session, produto: ProdutoCreate):

        if not produto.nome or produto.nome.strip() == "":
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Nome do produto é obrigatório.")
        
        if produto.preco <= 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preço deve ser maior que zero.")


        if hasattr(produto, "tamanhos") and produto.tamanhos:
            tamanhos_validos = {"PP", "P", "M", "G", "GG", "XG"} 
            for tamanho in produto.tamanhos:
                if tamanho not in tamanhos_validos:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"Tamanho inválido: {tamanho}. Tamanhos válidos: {tamanhos_validos}"
                    )

        novo_produto = ProdutoRepository.create_produto_repository(db=db, produto=produto)
        return novo_produto
