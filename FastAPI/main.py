from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str


@app.get('/')
async def root():
    return {'message':'Welcome to my API devlopemt'}
@app.get('/sign_in')
async def sign_in():
    return {'welcome':'you are sign in'}

@app.post('/createPost')
def createPost(new_post:Post):
    return new_post