from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from services import (
    CourseService,
    LanguageService,
    LessonService,
    SectionService,
    VocabularyService,
)


DBSession = Annotated[
    AsyncSession,
    Depends(get_db),
]


def get_language_service(
    db: DBSession,
) -> LanguageService:
    return LanguageService(db)


def get_course_service(
    db: DBSession,
) -> CourseService:
    return CourseService(db)


def get_lesson_service(
    db: DBSession,
) -> LessonService:
    return LessonService(db)


def get_section_service(
    db: DBSession,
) -> SectionService:
    return SectionService(db)


def get_vocabulary_service(
    db: DBSession,
) -> VocabularyService:
    return VocabularyService(db)


LanguageServiceDep = Annotated[
    LanguageService,
    Depends(get_language_service),
]

CourseServiceDep = Annotated[
    CourseService,
    Depends(get_course_service),
]

LessonServiceDep = Annotated[
    LessonService,
    Depends(get_lesson_service),
]

SectionServiceDep = Annotated[
    SectionService,
    Depends(get_section_service),
]

VocabularyServiceDep = Annotated[
    VocabularyService,
    Depends(get_vocabulary_service),
]
