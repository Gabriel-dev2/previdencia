from sqlalchemy import create_engine, MetaData
from config.config import DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_NAME

DATABASE_URL = f'mysql+pymysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:3306/{DATABASE_NAME}'
engine = create_engine(DATABASE_URL)
meta = MetaData()
conn = engine.connect()