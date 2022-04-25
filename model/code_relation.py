from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from configs.database import Base


class score(Base):
    __tablename__ = "code_score"
    file_path = Column(String, primary_key=True, unique=True)
    author = Column(String)
    dynamic = Column(String)
    discription = Column(String)
    dict_score = Column(String)
    # TODO set the score as same as problems
