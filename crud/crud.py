from operator import mod
from sqlalchemy.orm import Session
import model.code_relation as model
import document.schemas as schemas  # schemas???


def create_relation(db: Session, author: schemas.code_author):
    db_data = model.score(file_path=author.file_path, author=author.author,
                          dynamic=author.dynamic, discription=author.discription)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)


def save_score(author: schemas.code_author, db: Session):
    db_data = model.score(file_path=author.file_path, author=author.author,
                          dynamic=author.dynamic, discription=author.discription, dict_score=author.score)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
