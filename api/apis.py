import document.schemas as schemas
import service.service as service
from typing import List
from fastapi import File, Depends
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from configs.database import get_db
from configs.database import get_db

import json
routers = APIRouter()


@routers.post("/evaluation/")
def evaluation(author: str, dynamic: str, discription: str, file: bytes = File(...), db: Session = Depends(get_db)):
    author_model = schemas.code_author(
        author=author, discription=discription, dynamic=dynamic)
    author = service.code_upload(author_model, file)

    service.revised_code(author.file_path, author)
    #score = service.test()
    try:
        score = service.test()
    except:
        raise HTTPException(status_code=404, detail="code error")
    author.score = score

    service.save_data(author, db)
    json.loads(score)
    return author


# @routers.post("/start/")
# def start(ok: bool):
#    return service.test()


# @routers.get("/")
# def root():
#     return {"message": "Hello World"}
