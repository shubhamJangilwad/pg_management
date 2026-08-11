from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


DATABASE_URL = ("postgresql://postgres:12345@localhost:5432/pg_management"
)



engine = create_engine(DATABASE_URL)

Sessionlocal = sessionmaker(
    autocommit = False,
    autoflush= False,
    bind= engine
)


def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close

Base = declarative_base()
