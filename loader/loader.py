
import model.code_relation as models
from configs.database import engine

models.Base.metadata.create_all(bind=engine)  # bulit db with the models file
