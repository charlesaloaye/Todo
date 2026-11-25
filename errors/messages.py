from fastapi import HTTPException, status


def _not_found():
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")


def _unauthorized():
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized Request"
    )


def _invalid_credentials():
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )


def _already_exists():
    return HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Already Exists")
