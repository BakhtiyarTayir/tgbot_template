from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/eshopbot")

# engine = create_engine("mysql+mysqlconnector://root:@localhost/test_db", echo=True)

Base = declarative_base()

Base.metadata.create_all(engine)