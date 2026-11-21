from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DB_CONNECTION_URI = "sqlite:///./todosapp.db"


engine = create_engine(
    DB_CONNECTION_URI,
    connect_args={
        "check_same_thread": False,
    },
)


SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


Base = declarative_base()
