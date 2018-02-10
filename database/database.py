from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .models import *

url = 'postgresql://{}:{}@{}:{}/{}'
url = url.format('eshhkere', '0ea9e7d1-2077-4282-91e1-d8f6c15be421', 'localhost', 5432, 'eshhkerap')
engine = create_engine(url, convert_unicode=True)
Base = declarative_base()
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base.query = db_session.query_property()


def init_db():
    Base.metadata.create_all(bind=engine)
