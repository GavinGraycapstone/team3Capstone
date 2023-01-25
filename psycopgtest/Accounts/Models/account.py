from pydantic import BaseModel
from Accounts.Models.customer import Customer

class Account(BaseModel):
    id: int
    account_number: str
    customer: Customer
    current_balance: float