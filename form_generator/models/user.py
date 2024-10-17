from odmantic import Model
import pymongo

class User(Model):
    name: str
    email: str
    photo: str

    model_config = {
        "collection": "user",
        "indexes": lambda: [
            pymongo.IndexModel([("email", pymongo.ASCENDING)])
        ]
    }