from pydantic import BaseModel, Field

class CreateUser(BaseModel):
    name: str
    email: str
    password: int
class User(CreateUser):
    id: int
    class Config:
        orm_mode = True