from pydantic import BaseModel

class NewsItemCreate(BaseModel):
    title: str
    content: str

class NewsItemResponse(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        orm_mode = True
