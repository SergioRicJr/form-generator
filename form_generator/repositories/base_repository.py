import abc
from odmantic import AIOEngine, Model

class IRepository(metaclass=abc.ABCMeta):
    def __init__(self, session_factory) -> AIOEngine:
        self.session_factory = session_factory

class NosqlRepository(IRepository):
    model = Model

    async def get_all(self, filter: dict = None, sort=None):
        async with self.session_factory() as session:
            return await session.find(self.model, filter, sort=sort)

    async def get_all_paginated(self, filter: dict = None, sort=None, offset: int = 0, limit: int = 500):
        async with self.session_factory() as session:
            return await session.find(self.model, filter, sort=sort, skip=offset, limit=limit)

    async def get_count(self, filter: dict):
        async with self.session_factory() as session:
            return await session.count(self.model, filter)

    async def aggregate(self, group: dict, filters: dict):
        async with self.session_factory() as session:
            collection = session.get_collection(self.model)
            return await collection.aggregate([filters, group]).to_list(length=None)

    async def update_one(self, values: dict, filters: dict):
        async with self.session_factory() as session:
            collection = session.get_collection(self.model)
            return await collection.update_one(filters, {'$set': values})

    async def delete_one(self, filters: dict):
        async with self.session_factory() as session:
            collection = session.get_collection(self.model)
            return await collection.delete_one(filters)

    async def insert_one(self, values: dict):
        async with self.session_factory() as session:
            try:
                return await session.save(self.model(**values))
            except Exception as e:
                catch_exc = e

        raise catch_exc
    
    async def get_paginated_data(self, filter: dict, offset: int, limit: int):
        async with self.session_factory() as session:
            paginated_data = await session.find(self.model, filter, skip=offset, limit=limit)
            total = await session.count(self.model, filter)
            return paginated_data, total
