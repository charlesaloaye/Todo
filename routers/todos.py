from fastapi import APIRouter, Path, status

from db.database_service import db_dependency
from schemas.todo import TodoRequest, TodoResponse
from services import todo_service
from services.auth_service import CurrentUser

router = APIRouter(prefix="/todos", tags=["Todos"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[TodoResponse])
def read_all_todos(db: db_dependency):
    return todo_service.read_todos(db)


@router.get("/{todo_id}", status_code=status.HTTP_200_OK, response_model=TodoResponse)
def read_a_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    return todo_service.read_a_todo(db, todo_id)


@router.get(
    "/status/{todo_status}",
    status_code=status.HTTP_200_OK,
    response_model=list[TodoResponse],
)
def read_todo_by_status(db: db_dependency, todo_status: bool):
    return todo_service.read_todo_by_status(db, todo_status)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TodoResponse)
def create_todo(db: db_dependency, todo_request: TodoRequest, user: CurrentUser):
    return todo_service.create_todo(db, todo_request, user)


@router.put("/{todo_id}", status_code=status.HTTP_200_OK, response_model=TodoResponse)
def update_todo(
    db: db_dependency,
    todo_request: TodoRequest,
    user: CurrentUser,
    todo_id: int = Path(gt=0),
):
    return todo_service.update_todo(db, todo_request, todo_id, user)


@router.delete(
    "/{todo_id}", status_code=status.HTTP_200_OK, response_model=TodoResponse
)
def delete_todo(db: db_dependency, user: CurrentUser, todo_id: int = Path(gt=0)):
    return todo_service.delete_todo(db, todo_id, user)
