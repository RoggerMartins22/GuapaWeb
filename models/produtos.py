from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from database.base import Base

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String)
    preco = Column(Float, nullable=False)
    tamanhos = Column(ARRAY(String))
