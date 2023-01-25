from Accounts.Models.account import Account
from Accounts.Repositories.account import AccountRepository
from Accounts.Repositories.customer import CustomerRepository
from Accounts.Repositories.address import AddressRepository 


class AccountService():
    def __init__(self, account_repository: AccountRepository, 
            customer_repository: CustomerRepository,
            address_repository: AddressRepository) -> None:
        self.account_repository = account_repository
        self.customer_repository = customer_repository
        self.address_repository = address_repository

    def get_account(self, account_number: str) -> Account:
        account = self.account_repository.get_by_account_number(account_number)
        account.customer = self.customer_repository.get_by_id(account.customer.id)
        account.customer.address = self.address_repository.get_by_id(account.customer.address.id)
        return account

    def open_account(self, account: Account) -> Account:
        address = self.address_repository.insert(account.customer.address)
        account.customer.address = address
        customer = self.customer_repository.insert(account.customer)
        account.customer = customer
        return self.account_repository.insert(account)

    def get_all_accounts(self) -> 'list[Account]':
        accounts = self.account_repository.get_all()
        for account in accounts:
            account.customer = self.customer_repository.get_by_id(account.customer.id)
            account.customer.address = self.address_repository.get_by_id(account.customer.address.id)
        return accounts
        
    def withdraw(self, account_number: str, amount: float) -> Account:
        account = self.account_repository.get_by_account_number(account_number)
        account.current_balance -= amount
        self.account_repository.update(account)
        return self.get_account(account_number)

    def deposit(self, account_number: str, amount: float) -> Account:
        account = self.account_repository.get_by_account_number(account_number)
        account.current_balance += amount
        self.account_repository.update(account)
        return self.get_account(account_number)

    def close_account(self, account_number: str) -> None:
        account = self.get_account(account_number)
        self.account_repository.delete(account.id)
        self.customer_repository.delete(account.customer.id)
        self.address_repository.delete(account.customer.address.id)