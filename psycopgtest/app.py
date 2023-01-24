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


@app.get("/api/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/api/account/{account_id}")
def get_account_id(account_id: int ):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM account')
        result = cursor.fetchone()
        return result

@app.get("/api/address/{account_id}")
def get_account_id(account_id: int ):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM address')
        result = cursor.fetchone()
        return result

@app.get("/api/customer/")
def get_account_id():
    with connection.cursor() as cursor:
        cursor.execute('SELECT FirstName FROM customer where ID=11')
        result = cursor.fetchone()
        return result

# @app.post('/api/account/new')
# def create_account(account_id: int):
#     with connection.cursor() as cursor:
#         cursor.execute('INSERT INTO account (AccountNumber,CustomerID,CurrentBalance) VALUES (1, 1, 100);')
#         result = cursor.fetchone()
#         print(result)
#         return result

@app.post('/api/account/new')
def create_account(account_id: int):
    with connection.cursor() as cursor:
        cursor.execute('INSERT INTO address ( Address ,City,State ,ZipCode ) VALUES ( \'White house\', \'irvine\', \'CA\', \'9171\');')
        cursor.execute('INSERT INTO customer (FirstName, LastName, AddressID, Email) VALUES (\'Gavin2\', \'Gray2\', 1, \'gavg@capgroup.com\');')
        cursor.execute('INSERT INTO account ( AccountNumber, CustomerID,CurrentBalance) VALUES (1, 1, 100);')
        # cursor.execute('SELECT * FROM customer;')
        # result = cursor.fetchone()
        # print(result)
        return 'Object Created succesfully'

# @app.post('/api/account/new')
# def create_account(account_id: int):
#     with connection.cursor() as cursor:
#         cursor.execute('INSERT INTO account (AccountNumber,CustomerID,CurrentBalance) VALUES (1, 1, 100);')
#         result = cursor.fetchone()
#         print(result)
#         return result

# @app.post('/api/account/new')
# def create_account(account_id: int):
#     with connection.cursor() as cursor:
#         cursor.execute('INSERT INTO account (AccountNumber,CustomerID,CurrentBalance) VALUES (1, 1, 100);')
#         result = cursor.fetchone()
#         print(result)
#         return result

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True, timeout_keep_alive=3600, workers=10)