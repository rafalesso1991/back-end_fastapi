from pydantic import BaseModel, Field

class CreateBook(BaseModel):
    name: str = Field(..., min_length=2, max_length=30, regex="^[a-zA-Z0-9]+$")
    desc: str = Field(..., min_length=2, max_length=30)
    owner_id: int = Field(default=1, gt=0, lt=10)
class Book(CreateBook):
    id: int
    class Config:
        orm_mode = True