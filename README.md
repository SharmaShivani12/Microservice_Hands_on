Client ──▶ /users endpoint (routes.py)
              │
              ▼
      Validate request (models.py)
              │
              ▼
      Read/write user data (storage.py)
              │
              ▼
        JSON response (main.py)



This project was created as part of a hands-on activity to explore building a simple microservice using FastAPI and Docker. It simulates basic user operations using an in-memory store and serves as a foundational learning experience in designing and containerizing RESTful APIs
