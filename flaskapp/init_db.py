from sqlalchemy import create_engine 
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql.expression import text

username = 'indiuser'
password = 'indi1004'
host = 'localhost'
database = 'indidb'
# mysql_url = f"mariadb+pymysql://{username}:{password}@{host}/{database}?charset=utf8"  #문자열 포맷팅 적용 두가지 예
mysql_url = "mariadb+pymysql://{username}:{password}@{host}/{database}?charset=utf8".format(
    username = username, 
    password = password,
    host = host, 
    database = database
)
engine = create_engine(mysql_url)
# engine = create_engine(mysql_url, echo=True, convert_unicode=True, connect_args={"options": "-c timezone=utc"})

# Declare & create Session
db_session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))

# Create SqlAlchemy Base Instance
Base = declarative_base()
Base.query = db_session.query_property()

def init_database():
    Base.metadata.create_all(bind=engine)
