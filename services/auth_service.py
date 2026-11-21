from datetime import UTC, datetime, timedelta
from typing import Annotated

import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from core.config import settings
from db.database_service import db_dependency
from errors.messages import _already_exists, _invalid_credentials
from models.user import Users
from schemas.user import UserRequest
from security.password import verify

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


# pwd_context = context.CryptContext(schemes=["bcrypt"])


def create_user_token(user: Users) -> str:

    expire = datetime.now(UTC) + timedelta(minutes=settings.access_expiry_time)

    payload = {"sub": str(user.id), "role": str(user.role), "exp": expire}

    return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)


def get_current_user(
    db: db_dependency,
    token: Annotated[str, Depends(oauth2_scheme)],
):

    try:
        payload = jwt.decode(
            token, settings.secret_key, algorithms=[settings.algorithm]
        )

        user_id = int(payload["sub"])
    except (jwt.InvalidTokenError, KeyError, ValueError):
        raise _invalid_credentials()

    user = db.query(Users).filter(Users.id == user_id).first()

    if user is None:
        raise _invalid_credentials()

    return user


def register(db: Session, user_request: UserRequest):

    existing_user = (
        db.query(Users)
        .filter(
            (Users.username == user_request.username)
            | (Users.email == user_request.email)
        )
        .first()
    )

    if existing_user is not None:
        raise _already_exists()

    # New user object
    new_user = Users(
        username=user_request.username,
        email=user_request.email,
        status=user_request.status,
        hashed_password=hash_password(user_request.password),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def login(db: Session, username: str, password: str):

    user = db.query(Users).filter(Users.username == username).first()

    if not user or not verify(password, user.hashed_password):
        raise _invalid_credentials()

    token = create_user_token(user)

    return {"access_token": token, "token_type": "bearer"}


CurrentUser = Annotated[Users, Depends(get_current_user)]
