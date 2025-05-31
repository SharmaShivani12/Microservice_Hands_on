Client ──▶ /users endpoint (routes.py)
              │
              ▼
      Validate input/output (models.py)
              │
              ▼
      Access data layer (storage.py)
              │
              ▼
Return Python dict/model → FastAPI converts to JSON
              │
              ▼
         Response to client (main.py starts the app)




This project was created as part of a hands-on activity to explore building a simple microservice using FastAPI and Docker. It simulates basic user operations using an in-memory store and serves as a foundational learning experience in designing and containerizing RESTful APIs
