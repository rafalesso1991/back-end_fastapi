from config.config import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class BookModel(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    desc = Column(String, index=True)
    owner_id = Column(String, index=True)

    owner = relationship("UserModel")