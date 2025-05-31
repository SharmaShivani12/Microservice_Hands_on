## Basic Introduction

1. main.py creates the FastAPI app and includes routes from routes.py.

2. routes.py defines the endpoints. Each endpoint function:
Uses Pydantic models (models.py) to validate input/output.
Interacts with storage.py for data.
Returns a Python dict or model, which FastAPI automatically serializes to JSON.

3. FastAPI handles the actual JSON conversion and HTTP response


This project was created as part of a hands-on activity to explore building a simple microservice using FastAPI and Docker. It simulates basic user operations using an in-memory store and serves as a foundational learning experience in designing and containerizing RESTful APIs
