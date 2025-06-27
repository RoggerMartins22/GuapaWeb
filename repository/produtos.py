from sqlalchemy.orm import Session
from models.produtos import Produto
from schemas.produtos import ProdutoCreate

class ProdutoRepository:

    @staticmethod
    def create_produto_repository(db: Session, produto: ProdutoCreate):
        db_produto = Produto(
            nome=produto.nome,
            descricao=produto.descricao,
            preco=produto.preco,
            tamanhos=produto.tamanhos  
        )
        db.add(db_produto)
        db.commit()
        db.refresh(db_produto)
        return db_produto
