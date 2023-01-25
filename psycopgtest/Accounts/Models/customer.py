from pydantic import BaseModel
from Accounts.Models.address import Address

class Customer(BaseModel):
    id: int
    first_name: str
    last_name: str
    address: Address
    email_address: str