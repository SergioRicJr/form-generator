from datetime import datetime, timezone
from enum import Enum
from typing import List, Optional
from odmantic import Model, EmbeddedModel, Index, Field
from odmantic.query import asc, desc
import pymongo

class QuestionType(str, Enum):
    TEXT = "text"
    CHOICE = "choice"

class QuestionOptions(Model):
    id: str
    text: str

class Question(Model):
    score: float
    text: str
    qtype: QuestionType
    required: bool
    options: Optional[List[QuestionOptions]] = None
    answer: Optional[str]
    template: Optional[str]

class Form(Model):
    created_at: datetime = Field(default_factory=datetime.now())
    answered_at: Optional[datetime] = None
    creator: str
    receiver: str
    questions: List[Question]
    
    model_config = {
        "collection": "form",
        "indexes": lambda: [
            pymongo.IndexModel([(+Form.creator, pymongo.TEXT)]),
            pymongo.IndexModel([("created_at", pymongo.ASCENDING)]),
            pymongo.IndexModel([("answered_at", pymongo.ASCENDING)]),
        ]
    }