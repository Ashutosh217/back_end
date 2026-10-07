from pydantic import BaseModel

class PostCreate(BaseModel):
    title: str
    content: str
    userId: int



class Post(PostCreate):
    id: int


    