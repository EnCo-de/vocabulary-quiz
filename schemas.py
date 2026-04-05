"""The pydantic schemas"""

from pydantic import BaseModel


class Vocabulary(BaseModel):
    word: str
    translation: str
