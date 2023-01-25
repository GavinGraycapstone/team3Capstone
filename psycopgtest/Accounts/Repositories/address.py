import psycopg2
from Accounts.Models.address import Address


class AddressRepository():
    def insert(self, address: Address) -> Address:
        with psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password='password123',) as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO address 
                        (Address, City, State, ZipCode) VALUES
                        (%(address)s, %(city)s, %(state)s, %(zip_code)s)
                        RETURNING id
                    """, {
                    'address': address.address,
                    'city': address.city,
                    'state': address.state,
                    'zip_code': address.zip_code
                }
                )
                address.id = cursor.fetchone()[0]
        return address

    def get_by_id(self, id) -> Address:
        with psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password='password123',) as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    SELECT ID, Address, City, State, ZipCode FROM 
                        address WHERE ID=%(address_id)s
                    """, {
                    'address_id': id
                }
                )
                row = cursor.fetchone()
        return Address.construct(id=row[0], address=row[1], city=row[2], state=row[3], zip_code=row[4])

    def delete(self, id) -> None:
        with psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password='password123',) as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM address WHERE ID=%(address_id)s
                    """, {
                    'address_id': id
                }
                )