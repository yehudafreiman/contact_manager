# Contact Manager API

A simple REST API for managing contacts using FastAPI, MySQL, and Docker.

## What it does

This API lets you create, view, update, and delete contacts. All data is stored in a MySQL database.

## API Endpoints

- `GET /contacts` - Get all contacts
- `POST /contacts` - Create a new contact
- `PUT /contacts/{id}` - Update a contact
- `DELETE /contacts/{id}` - Delete a contact

## How to run

1. Clone your repository:
```bash
git clone <your-repo-url> test_submission
cd test_submission
```
2. Start the application:
```bash
docker compose up -d
```

3. Wait 30 seconds for database initialization
```bash
sleep 30
```
4. The API is now running at `http://localhost:8000`

## Testing

Get all contacts:
```bash
curl http://localhost:8000/contacts
```

Create a contact:
```bash
curl -X POST http://localhost:8000/contacts \
-H "Content-Type: application/json" \
-d '{"first_name":"Test","last_name":"User","phone_number":"050-9999999"}'
```

Update a contact:
```bash
curl -X PUT http://localhost:8000/contacts/4 \
-H "Content-Type: application/json" \
-d '{"phone_number":"052-8888888"}'
```

Delete a contact:
```bash
curl -X DELETE http://localhost:8000/contacts/4
```

Test data persistence:
```bash
docker compose down
docker compose up -d
sleep 30
curl http://localhost:8000/contacts # Should show original contacts
```

## Clean up
```bash
docker compose down -v
```