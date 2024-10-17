from os import getenv
from distutils.util import strtobool


class Config:
    MONGO_DATABASE_DB = getenv('MONGO_DATABASE_DB', 'shipay')
    MONGO_DATABASE_HOST = getenv('MONGO_DATABASE_HOST', 'localhost')
    MONGO_DATABASE_PORT = int(getenv('MONGO_DATABASE_PORT', 27017))
    MONGO_DATABASE_USER = getenv('MONGO_DATABASE_USER', 'shipay')
    MONGO_DATABASE_PASSWORD = getenv('MONGO_DATABASE_PASSWORD', '')
    MONGO_DATABASE_AUTH_SOURCE = getenv('MONGO_DATABASE_AUTH_SOURCE', 'admin')
    MONGO_USE_CONNECTION_STRING = bool(strtobool(getenv('MONGO_USE_CONNECTION_STRING', 'False')))
    MONGO_CONNECTION_STRING = getenv('MONGO_CONNECTION_STRING')