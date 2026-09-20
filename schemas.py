"""The pydantic schemas"""

from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field, field_validator

from models import Level


class SchemaBase(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )


# ============================================================================
# Language
# ============================================================================


class LanguageCreate(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    code: str = Field(min_length=2, max_length=10)

    @field_validator("name", "code", mode="before")
    @classmethod
    def normalize(cls, value: str) -> str:
        if isinstance(value, str):
            return " ".join(value.strip().split())

        return value


class LanguageResponse(SchemaBase):
    id: int
    name: str
    code: str


# ============================================================================
# Course
# ============================================================================


class CourseCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str | None = Field(
        default=None,
        max_length=500,
    )
    level: Level
    language_id: int = Field(gt=0)

    @field_validator("title", mode="before")
    @classmethod
    def normalize(cls, value: str) -> str:
        if isinstance(value, str):
            return " ".join(value.strip().split())
        return value


class CourseResponse(SchemaBase):
    id: int
    title: str
    description: str | None
    level: Level
    language_id: int


# ============================================================================
# Lesson
# ============================================================================


class LessonCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description:     description: str | None = Field(
        default=None,
        max_length=500,
    )
    position: int = Field(default=0, ge=0)
    course_id: int = Field(gt=0)

    @field_validator("title", mode="before")
    @classmethod
    def normalize(cls, value: str) -> str:
        if isinstance(value, str):
            return " ".join(value.strip().split())
        return value


class LessonResponse(SchemaBase):
    id: int
    title: str
    description: str | None
    position: int
    course_id: int


# ============================================================================
# Lesson Section
# ============================================================================


class SectionCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    position: int = Field(default=0, ge=0)
    lesson_id: int = Field(gt=0)

    @field_validator("title", mode="before")
    @classmethod
    def normalize_title(cls, value: str) -> str:
        if isinstance(value, str):
            return " ".join(value.strip().split())

        return value


class SectionResponse(SchemaBase):
    id: int
    title: str
    position: int
    lesson_id: int


# ============================================================================
# Vocabulary
# ============================================================================


class VocabularyCreate(BaseModel):
    word: str = Field(min_length=1, max_length=100)
    translation: str = Field(min_length=1, max_length=100)
    section_id: int = Field(gt=0)

    @field_validator("word", "translation", mode="before")
    @classmethod
    def normalize_text(cls, value: str) -> str:
        if isinstance(value, str):
            return " ".join(value.strip().split())

        return value


class VocabularyResponse(SchemaBase):
    id: int
    word: str
    translation: str
    section_id: int
