#  Defines the data model for user input and output.

from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
