from dependency_injector import containers, providers
from form_generator.infrastructure.database.database import MongoDatabase
from form_generator.repositories.form_repository import FormRepository
from form_generator.repositories.user_repository import UserRepository


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    mongo_database = providers.Singleton(
        MongoDatabase, database="lathe_monitoring", host="127.0.0.1", port=27017
    )

    form_repository = providers.Singleton(
        FormRepository, session_factory=mongo_database.provided.session
    )

    user_repository = providers.Singleton(
        UserRepository, session_factory=mongo_database.provided.session
    )

    