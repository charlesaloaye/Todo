from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DB_CONNECTION_URI = "postgresql://postgres:password@localhost/TodoApplicationDatabase"


engine = create_engine(DB_CONNECTION_URI)


SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


Base = declarative_base()
