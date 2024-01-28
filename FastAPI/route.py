from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str

@app.get('/')
def route():
    return {"Name": "Parbat Budha"}

@app.post('/Post')
def newsfeed(feed:Post):
    return feed

