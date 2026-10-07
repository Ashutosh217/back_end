from fastapi import FastAPI, HTTPException
from models import Post, PostCreate

app = FastAPI()

posts_db: list[Post] = [
    Post(id=1, title="First Post", content="Hello world", userId=1),
    Post(id=2, title="Second Post", content="Learning FastAPI", userId=1),
]

next_id = 3

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts() -> list[Post]:
    return posts_db

@app.get("/posts/{post_id}")
def get_post(post_id: int) -> Post:
    post = next((p for p in posts_db if p.id == post_id), None)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.post("/posts", status_code=201)
def create_post(post: PostCreate) -> Post:
    global next_id
    new_post = Post(id=next_id, **post.model_dump())
    posts_db.append(new_post)
    next_id += 1
    return new_post