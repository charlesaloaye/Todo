from passlib import context

pwd_context = context.CryptContext(schemes=["bcrypt"])


def hash_password(plain: str) -> str:
    return pwd_context.hash(plain)


def verify(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)
