from pydantic import BaseModel


class code_author(BaseModel):
    file_path: str = "string"
    score: str = "none"
    author: str
    discription: str
    dynamic: str

    class Config:
        orm_mode = True
