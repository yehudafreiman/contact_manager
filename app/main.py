from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="contact_manager")

# models
class ContactCreate(BaseModel):
    first_name: str
    last_name: str
    phone_number: str

class ContactUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    phone_number: str | None = None

# fake database
contacts = [
    {"id": 1, "first_name": "John", "last_name": "Doe", "phone_number": "050-1234567"},
    {"id": 2, "first_name": "Jane", "last_name": "Smith", "phone_number": "052-9876543"},
    {"id": 3, "first_name": "Bob", "last_name": "Johnson", "phone_number": "054-5555555"},
    {"id": 4, "first_name": "Jack", "last_name": "Robinson", "phone_number": "050-6115555"},
]

# READ
app.get("/contacts")
def get_all_contacts():
    return contacts

# POST
app.get("/contacts")
def create_new_contact(contact: ContactCreate):
    new_id = len(contacts) + 1
    new_contact = {
        "id": new_id,
        "first_name": contact.first_name,
        "last_name": contact.last_name,
        "phone_number": contact.phone_number
    }
    contacts.append(new_contact)
    return {"massage": "Contact created successfully",
            "id": new_id}

# PUT
app.get("/contacts/{id}")
def update_existing_contact(contact_id: int, update_contact: ContactUpdate):
    for contact in contacts:
        if contact["id"] == contact_id:
            if update_contact.first_name is not None:
                contacts["first_name"] = update_contact.first_name
            if update_contact.last_name is not None:
                contacts["last_name"] = update_contact.last_name
            if update_contact.phone_number is not None:
                contacts["phone_number"] = update_contact.phone_number
        return {"massage": "Contact update successfully"}
    raise HTTPException(status_code=404, detail="Contact not found")

# DELETE
app.get("/contacts/{id}")
def delete_contact(contact_id: int):
    for index, contact in enumerate(contacts):
        if contact["todo_id"] == contact_id:
            contacts.pop(index)
            return {"message": "Contact delete successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")

# RUN
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)