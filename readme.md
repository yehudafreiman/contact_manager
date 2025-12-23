
### 1. GET - קבלת כל אנשי הקשר
```bash
curl -X GET http://localhost:8000/contacts
```

### 2. POST - יצירת איש קשר חדש
```bash
curl -X POST http://localhost:8000/contacts \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "Sarah",
    "last_name": "Cohen",
    "phone_number": "053-1234567"
  }'
```

### 3. PUT - עדכון איש קשר קיים
```bash
curl -X PUT http://localhost:8000/contacts/1 \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "Jonathan",
    "last_name": "Doe",
    "phone_number": "050-9999999"
  }'
```

### 4. DELETE - מחיקת איש קשר
```bash
curl -X DELETE http://localhost:8000/contacts/3
```
