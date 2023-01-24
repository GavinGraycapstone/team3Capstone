from typing import Union
import psycopg2

from fastapi import FastAPI

app = FastAPI()

connection = psycopg2.connect(
    host="localhost",
    database="psycopgtest",
    user="postgres",
    password=None,
)
connection.set_session(autocommit=True)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

with connection.cursor() as cursor:
    cursor.execute('SELECT COUNT(*) FROM account')
    result = cursor.fetchone()
    print(result)