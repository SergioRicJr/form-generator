import abc
from contextlib import asynccontextmanager
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine

class IDatabase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def session(self):
        pass

class MongoDatabase(IDatabase):
    def __init__(self, database: str, host: str, port: str) -> None:
        self.database = database
        self.host = host
        self.port = port
        self._conn_string = f'mongodb://{self.host}:{self.port}'
        self.motor_client = AsyncIOMotorClient(self._conn_string)
        self._session_factory = AIOEngine(client=self.motor_client, database=self.database)
        

    @asynccontextmanager
    async def session(self):
        session = self._session_factory
        try:
            yield session
        except Exception:
            raise