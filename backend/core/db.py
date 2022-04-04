from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import settings

SQLALCHEMY_DATABASE_URL = settings.db_url

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,echo=True,
    connect_args={'check_same_thread':False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



def get_db() -> SessionLocal:
    """
    Get db to create session
    :return Session:
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @event.listens_for(Engine, "before_execute")
# def my_before_execute(
#         conn, clauseelement, multiparams, params, execution_options
# ):
#     print("before execute!")
#
# @event.listens_for(Engine, "after_execute")
# def my_before_execute(
#         conn, clauseelement, multiparams, params, execution_options
# ):
#     print("after execute!")