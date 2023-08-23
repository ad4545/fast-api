from fastapi import FastAPI, Body
import uvicorn
from models import PostSchema, UserLoginSchema, UserSchema
from auth.jwt_handler import signJWT

posts = [
    {
        "id": 1,
        "title": "Hello-1",
        "text": "Thank You-1"
    },
    {
        "id": 2,
        "title": "Hello-2",
        "text": "Thank You-2"
    },
    {
        "id": 3,
        "title": "Hello-3",
        "text": "Thank You-3"
    }
]

users = []

app = FastAPI()


@app.get('/', tags=["test"])
def entry():
    return {"Hello": "World"}

# get posts


@app.get('/posts', tags=['posts'])
def get_posts():
    return {"data": posts}

# get_one_post


@app.get('/posts/{id}', tags=["posts"])
def get_one(id: int):
    if id > len(posts):
        return {
            "error": "Not found"
        }

    for item in posts:
        if item['id'] == id:
            return {"data": item}

# create post


@app.post('/post', tags=['posts'])
def add_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())

    return {
        "created": post
    }


def check_user(data: UserLoginSchema):
    for item in users:
        if item.email == data.email and item.password == data.password:
            return True
        else:
            return False

# authentication


@app.post('/signup', tags=['auth'])
def sign_up(user: UserSchema = Body(default=None)):
    users.append(user)
    return signJWT(user.email)


@app.post('/login', tags=['auth'])
def login(user: UserLoginSchema = Body(default=None)):
    if check_user(user):
        return {
            "message": "Login successful"
        }
    else:
        return {
            "message": "Error"
        }
