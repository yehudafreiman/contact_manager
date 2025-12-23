import mysql.connector
import os
from typing import Optional


# initial a contact
class Contact:
    def __init__(self, id: int, first_name: str, last_name: str, phone_number: str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    # turn object to a dictionary
    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number
        }

# create database connection
def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        port=int(os.getenv("DB_PORT", 3306)),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "mysqlmysql"),
        database=os.getenv("DB_NAME", "contacts")
    )
    return connection

# create new contact
def create_contact(first_name: str, last_name: str, phone_number: str) -> int:
    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
            INSERT INTO contacts (first_name, last_name, phone_number)
            VALUES (%s, %s, %s) \
            """
    cursor.execute(query, (first_name, last_name, phone_number))

    connection.commit()
    new_id = cursor.lastrowid
    cursor.close()
    connection.close()
    return new_id

# get all contacts
def get_all_contacts() -> list[Contact]:
    connection = get_db_connection()
    cursor = connection.cursor()

    query = "SELECT id, first_name, last_name, phone_number FROM contacts"
    cursor.execute(query)

    results = cursor.fetchall()
    contacts = [Contact(id=row[0], first_name=row[1], last_name=row[2], phone_number=row[3]) for row in results]

    cursor.close()
    connection.close()
    return contacts

# update a contact
def update_contact(contact_id: int,
                   first_name: Optional[str] = None,
                   last_name: Optional[str] = None,
                   phone_number: Optional[str] = None) -> bool:
    connection = get_db_connection()
    cursor = connection.cursor()

    updates = []
    params = []
    if first_name is not None:
        updates.append("first_name = %s")
        params.append(first_name)
    if last_name is not None:
        updates.append("last_name = %s")
        params.append(last_name)
    if phone_number is not None:
        updates.append("phone_number = %s")
        params.append(phone_number)
    if not updates:
        return False

    params.append(contact_id)

    query = f"UPDATE contacts SET {', '.join(updates)} WHERE id = %s"
    cursor.execute(query, params)

    success = cursor.rowcount > 0
    cursor.close()
    connection.close()
    return success

# delete a contact
def delete_contact(contact_id: int) -> bool:
    connection = get_db_connection()
    cursor = connection.cursor()

    query = "DELETE FROM contacts WHERE id = %s"
    cursor.execute(query, (contact_id,))

    connection.commit()
    success = cursor.rowcount > 0
    cursor.close()
    connection.close()
    return success

