from typing import Type

from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker

from database.creator import RequestTable


class RequestWorker:
    def __init__(self, database_url: str):
        engine = create_engine(database_url)
        self.__session = sessionmaker(engine)

    def add_request(self, request: RequestTable):
        with self.__session() as session:
            session.add(request)
            session.commit()

    def get_last_rows(self, count: int) -> list[Type[RequestTable]]:
        with self.__session() as session:
            return session.query(RequestTable).order_by(desc(RequestTable.id)).limit(count).all()
