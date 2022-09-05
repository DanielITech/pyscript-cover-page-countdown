
from typing import Union

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open('home.html', 'r') as ind:
        data = ind.read()
    return HTMLResponse(data)


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
