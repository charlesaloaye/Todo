from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from db.database_service import db_dependency
from schemas.user import UserRequest, UserResponse
from services import auth_service

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", status_code=status.HTTP_200_OK, response_model=UserResponse)
def create_account(db: db_dependency, user_request: UserRequest):
    return auth_service.register(db, user_request)


@router.post("/token")
def login_for_token(
    db: db_dependency, formdata: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    return auth_service.login(db, formdata.username, formdata.password)
