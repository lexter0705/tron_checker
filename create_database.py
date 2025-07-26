from sqlalchemy import create_engine

from config import get_config
from database.creator import Base


def create_database():
    config = get_config()
    engine = create_engine(config.database_url)
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_database()
