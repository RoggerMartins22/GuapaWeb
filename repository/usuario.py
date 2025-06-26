from sqlalchemy.orm import Session
from models.usuario import Usuario

class UserRepository:
    @staticmethod
    def consulta_usuario_por_id(db: Session, usuario_id: int):
        return db.query(Usuario).filter(Usuario .id == usuario_id).first()   

    @staticmethod
    def consulta_usuario_por_cpf(db: Session, cpf: str):
        return db.query(Usuario).filter(Usuario.cpf == cpf).first()