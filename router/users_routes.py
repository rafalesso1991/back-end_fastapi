from fastapi import APIRouter
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from config.config import get_db
from models.user_model import UserModel
from schemas.user_schema import CreateUser, User

users_router = APIRouter()

users_router = SQLAlchemyCRUDRouter(
    schema=User,
    create_schema=CreateUser,
    db_model=UserModel,
    db=get_db,
    create_route=False,
    update_route=False,
    delete_one_route=False,
    delete_all_route=False,
    prefix="/users",
    tags=["Users"]
)