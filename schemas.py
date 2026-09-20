"""The pydantic schemas"""

from pydantic import BaseModel, ConfigDict, Field, field_validator

from models import Level


class LanguageCreate(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    code: str = Field(min_length=2, max_length=10)

    @field_validator("name", "code", mode="before")
    @classmethod
    def normalize(cls, value: str) -> str:
        if isinstance(value, str):
            return " ".join(value.strip().split())
        return value


class CourseCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str | None = None
    level: Level
    language_id: int

    @field_validator("title", mode="before")
    @classmethod
    def normalize(cls, value: str) -> str:
        if isinstance(value, str):
            return " ".join(value.strip().split())
        return value


class LessonCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str | None = None
    position: int = Field(default=0, ge=0)
    course_id: int

    @field_validator("title", mode="before")
    @classmethod
    def normalize(cls, value: str) -> str:
        if isinstance(value, str):
            return " ".join(value.strip().split())
        return value

class SectionCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    position: int = Field(default=0, ge=0)
    lesson_id: int

    @field_validator("title", mode="before")
    @classmethod
    def normalize(cls, value: str) -> str:
        if isinstance(value, str):
            return " ".join(value.strip().split())
        return value


class VocabularyCreate(BaseModel):
    word: str = Field(min_length=1, max_length=100)
    translation: str = Field(min_length=1, max_length=100)
    section_id: int

    @field_validator("word", "translation", mode="before")
    @classmethod
    def normalize(cls, value: str) -> str:
        if isinstance(value, str):
            return " ".join(value.strip().split())
        return value
