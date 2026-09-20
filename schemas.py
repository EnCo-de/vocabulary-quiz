"""The pydantic schemas"""

from pydantic import BaseModel, Field, field_validator


class Vocabulary(BaseModel):
    word: str = Field(min_length=1)
    translation: str = Field(min_length=1)

    @field_validator("word", "translation", mode="before")
    @classmethod
    def normalize(cls, value: str) -> str:
        if isinstance(value, str):
            return " ".join(value.strip().split())
        return value
