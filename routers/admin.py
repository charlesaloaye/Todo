from fastapi import APIRouter, status

from db.database_service import db_dependency
from schemas.user import UserResponse
from services import auth_service
from services.auth_service import CurrentUser

router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get(
    "/users",
    status_code=status.HTTP_200_OK,
    response_model=list[UserResponse],
)
def read_all_users(db: db_dependency, user: CurrentUser):
    return auth_service.all_users(db, user)


@router.get(
    "/users/{user_id}", status_code=status.HTTP_200_OK, response_model=UserResponse
)
def read_a_user(db: db_dependency, user_id: int, user: CurrentUser):
    return auth_service.read_a_user(db, user_id, user)
