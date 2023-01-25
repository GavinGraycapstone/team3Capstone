import psycopg2
from Accounts.Models.account import Account
from Accounts.Models.customer import Customer


class AccountRepository():
 
    def insert(self, account: Account) -> Account:
        with psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password='password123',) as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO account 
                        (AccountNumber, CustomerID, CurrentBalance) VALUES
                        (%(account_number)s, %(customer_id)s, %(current_balance)s)
                        RETURNING id
                    """, {
                    'account_number': account.account_number,
                    'customer_id': account.customer.id,
                    'current_balance': account.current_balance
                }
                )
                account.id = cursor.fetchone()[0]
        return account

    def get_by_account_number(self, account_number: str) -> Account:
        with psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password='password123',) as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    SELECT ID, AccountNumber, CustomerID, CurrentBalance FROM 
                        account WHERE AccountNumber=%(account_number)s
                    """, {
                    'account_number': account_number
                }
                )
                row = cursor.fetchone()
        return Account.construct(id=row[0], account_number=row[1], customer=Customer.construct(id=row[2]), current_balance=round(row[3], 2))

    def get_all(self) -> 'list[Account]':
        results = []
        with psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password='password123',) as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    SELECT ID, AccountNumber, CustomerID, CurrentBalance FROM account
                    """)
                rows = cursor.fetchall()
        for row in rows:
            results.append(Account.construct(id=row[0], account_number=row[1], customer=Customer.construct(
                id=row[2]), current_balance=round(row[3], 2)))
        return results

    def update(self, account: Account) -> None:
        with psycopg2.connect(
            host="localhost",
            database="psycopgtest",
            user="postgres",
            password='password123',) as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    UPDATE account 
                        SET AccountNumber=%(account_number)s, CustomerID=%(customer_id)s, CurrentBalance=%(current_balance)s
                        WHERE ID=%(id)s
                    """, {
                    'id': account.id,
                    'account_number': account.account_number,
                    'customer_id': account.customer.id,
                    'current_balance': account.current_balance
                }
                )

    def delete(self, id) -> None:
        with psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password='password123',) as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM account WHERE ID=%(account_id)s
                    """, {
                    'account_id': id
                }
                )