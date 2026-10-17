from sqlalchemy import create_engine

DB_URL = "postgresql+psycopg2://admin:password123@localhost:5434/olist_db"

def get_engine():
    return create_engine(DB_URL)