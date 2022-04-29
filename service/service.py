import crud.crud as crud
import document.schemas as schemas
import datetime
from sqlalchemy.orm import Session
from fastapi import File, HTTPException
import importlib
import json


def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj.__dict__


def name_create(author: schemas.code_author):
    file_path = author.dynamic + datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    save_name = "Codes/"+file_path+".py"
    return save_name, file_path


def creat_dbrelation(author: schemas.code_author):
    crud.create_relation()


def code_upload(author: schemas.code_author, file: bytes = File(...)):
    save_name, file_path = name_create(author)
    author.file_path = file_path
    with open(save_name, "wb") as f:
        f.write(file)
    return author


def save_data(author: schemas.code_author, db: Session):
    crud.save_score(author=author, db=db)

# -------------------------


def revised_code(testing_code: str, author: schemas.code_author):
    f = open("service/testing.py", "r")  # TODO file name
    content = f.readlines()
    f.close()
    content[0] = "from Codes."+author.file_path + \
        " import SyncMapX\n"  # TODO what to revise
    f = open("service/testing.py", "w")
    f.writelines(content)
    f.close()


def test():

    import service.testing as testing
    return json.dumps(testing.normal_test_muti())


def testing_package(author: schemas.code_author, db: Session):
    revised_code(author.file_path, author)
    try:
        socre = test()
    except:
        raise HTTPException(status_code=404, detail="code error")
    author.score = socre
    save_data(author, db)
