# Student Support Ticket API
A FastAPI-based backend application for managing student support tickets using **JWT authentication**, **in-memory storage**, and **Loguru logging**.

---

## Features
- JWT-based authentication
- User login with in-memory users
- Ticket creation & retrieval
- Admin ticket updates (status & priority)
- Dependency Injection with FastAPI
- Structured logging using **Loguru**
- Clean separation of concerns
---
## Tech Stack
- **Python 3.10+**
- **FastAPI**
- **Pydantic**
- **JWT (python-jose)**
- **Loguru**
- **Uvicorn**
---

## Project Structure
```text
    ├── src/
    │  ├── in_memory_db
    │  │    └── in_memory_users
    │  │    └── in_memory_tickets  
    │  ├── logs
    │  │    └── app.log
    │  ├── models/
    │  │    └── user.py
    │  │    └── tickets.py     
    │  ├── routes/
    │  │    └── auth.py
    │  │    └── user.py  
    │  ├── schemas
    │  │    └── tickets.py
    │  │    └── user.py 
    │  ├── utils
    │  │    ├── generators
    │  │    │    └── secret_key_generator.py
    │  │    │    └── ticket_id_generator.py 
    │  │    └── jwt_handaller.py
    │  │    └── logger.py   
    │  └── main.py      
    └── .gitignore
    └── README.md
    └── requirements.txt
```
### Design 
  * Schemas → API validation & serialization
  * In-memory DB → temporary persistence layer
  * Dependencies → authentication & security
  * Utils → shared helpers (JWT, logging)
  * Routes → request handling only
---
### Authentication Flow
1. User logs in using email & password
2. Server validates credentials from in-memory users
3. JWT token is generated and returned
4. Client sends token in `Authorization` header
5. Protected routes extract and verify token using dependencies.
___
### Logging (Loguru)
* Logs are written to:
    * Console (stdout)
    * File: src/logs/app.log
* Features:
  * Auto rotation
  * Retention policy
  * Compression
  * Thread-safe logging
___
## API Endpoints
### Authentication
| Method | Endpoint | Auth Required | Description                       |
| ------ | -------- | ------------- | --------------------------------- |
| POST   | `/login` | ❌ No          | Login user and generate JWT token |

### Ticket Management
| Method | Endpoint               | Auth Required | Role          | Description                                                                     |
| ------ | ---------------------- | --------- |---------------|---------------------------------------------------------------------------------|
| POST   | `/tickets/create`      | ✅ Yes     | Student/Admin | Create a new support ticket                                                     |
| GET    | `/tickets/all`         | ✅ Yes     | Student/Admin | Get all tickets created by the logged-in user,<br/>for admin role obtain all tickets |
| GET    | `/tickets/{ticket_id}` | ✅ Yes     | Studnet/Admin | Get ticket details by ticket ID                                                 |
| PATCH  | `/tickets/{ticket_id}` | ✅ Yes     | Admin         | Update ticket status and priority                                               |
___
##  Steps to Run the Project
### 1. Clone the Repository
```terminaloutput
    git clone https://github.com/DEBDEEPTA/STUDENT-SUPPORT-TICKET-API.git
    cd StudentSupportTicketAPI
```
### 2. Install Dependencies
```terminaloutput
    pip install -r src/requirements.txt
```
### 3. Run the FastAPI Server
```terminaloutput
    uvicorn src.main:app --reload
```
