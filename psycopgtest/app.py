from typing import Union
import psycopg2
import uvicorn
from fastapi import FastAPI

app = FastAPI()

connection = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password='password123',
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

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True, timeout_keep_alive=3600, workers=10)