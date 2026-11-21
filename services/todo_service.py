from sqlalchemy.orm import Session

from errors.messages import _already_exists, _not_found
from models.todo import Todos
from schemas.todo import TodoRequest


def read_todos(db: Session):
    return db.query(Todos).filter(Todos.is_public == True).all()


def read_a_todo(db: Session, todo_id: int):

    existing_todo = db.query(Todos).filter(Todos.id == todo_id).first()

    if existing_todo is None:
        raise _not_found()

    return existing_todo


def read_todo_by_status(db: Session, todo_status: bool):

    existing_todo = db.query(Todos).filter(Todos.completed == todo_status).all()

    if existing_todo is None:
        raise _not_found()

    return existing_todo


# Auth Users only
def create_todo(db: Session, todo_request: TodoRequest, user: Session):

    existing_todo = db.query(Todos).filter(Todos.title == todo_request.title).first()

    if existing_todo is not None:
        raise _already_exists()

    new_todo = Todos(**todo_request.model_dump(), owner_id=user.id)

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return new_todo


def update_todo(db: Session, todo_request: TodoRequest, todo_id: int, user: Session):

    existing_todo = (
        db.query(Todos).filter((Todos.id == todo_id), (Todos.id == user.id)).first()
    )

    if existing_todo is None:
        raise _not_found()

    existing_todo.title = todo_request.title
    existing_todo.description = todo_request.description
    existing_todo.priority = todo_request.priority
    existing_todo.completed = todo_request.completed
    existing_todo.is_public = todo_request.is_public

    db.add(existing_todo)
    db.commit()
    db.refresh(existing_todo)

    return existing_todo


def delete_todo(db: Session, todo_id: int, user: Session):

    existing_todo = (
        db.query(Todos)
        .filter((Todos.id == todo_id) and (Todos.owner_id == user.id))
        .first()
    )

    if existing_todo is None:
        raise _not_found()

    db.delete(existing_todo)
    db.commit()

    return existing_todo
