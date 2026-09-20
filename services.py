from sqlalchemy.ext.asyncio import AsyncSession

from exceptions import ConflictError, NotFoundError
from models import (
    Course,
    Language,
    Level,
    Lesson,
    LessonSection,
    Vocabulary,
)
from repository import (
    CourseRepository,
    LanguageRepository,
    LessonRepository,
    SectionRepository,
    VocabularyRepository,
)
from schemas import (
    CourseCreate,
    LanguageCreate,
    LessonCreate,
    SectionCreate,
    VocabularyCreate,
)


class LanguageService:
    def __init__(self, db: AsyncSession):
        self.repository = LanguageRepository(db)

    async def create(
        self,
        data: LanguageCreate,
    ) -> Language:
        language = await self.repository.create(data)

        if language is None:
            raise ConflictError(
                f"Language '{data.code}' already exists."
            )

        return language

    async def get(
        self,
        language_id: int,
    ) -> Language:
        language = await self.repository.get(language_id)

        if language is None:
            raise NotFoundError(
                f"Language {language_id} not found."
            )

        return language

    async def get_by_code(
        self,
        code: str,
    ) -> Language:
        language = await self.repository.get_by_code(code)

        if language is None:
            raise NotFoundError(
                f"Language '{code}' not found."
            )

        return language

    async def list(self) -> list[Language]:
        return await self.repository.list()

    async def delete(
        self,
        language_id: int,
    ) -> None:
        deleted = await self.repository.delete(language_id)

        if not deleted:
            raise NotFoundError(
                f"Language {language_id} not found."
            )


class CourseService:
    def __init__(self, db: AsyncSession):
        self.repository = CourseRepository(db)

    async def create(
        self,
        data: CourseCreate,
    ) -> Course:
        course = await self.repository.create(data)

        if course is None:
            raise ConflictError(
                "Language not found or course already exists."
            )

        return course

    async def get(
        self,
        course_id: int,
    ) -> Course:
        course = await self.repository.get(course_id)

        if course is None:
            raise NotFoundError(
                f"Course {course_id} not found."
            )

        return course

    async def list(
        self,
        language_code: str,
        level: Level,
    ) -> list[Course]:
        return await self.repository.list(
            language_code=language_code,
            level=level,
        )

    async def list_all(self) -> list[Course]:
        return await self.repository.list_all()

    async def delete(
        self,
        course_id: int,
    ) -> None:
        deleted = await self.repository.delete(course_id)

        if not deleted:
            raise NotFoundError(
                f"Course {course_id} not found."
            )


class LessonService:
    def __init__(self, db: AsyncSession):
        self.repository = LessonRepository(db)

    async def create(
        self,
        data: LessonCreate,
    ) -> Lesson:
        lesson = await self.repository.create(data)

        if lesson is None:
            raise ConflictError(
                "Course not found or lesson already exists."
            )

        return lesson

    async def get(
        self,
        lesson_id: int,
    ) -> Lesson:
        lesson = await self.repository.get(lesson_id)

        if lesson is None:
            raise NotFoundError(
                f"Lesson {lesson_id} not found."
            )

        return lesson

    async def list(
        self,
        course_id: int,
    ) -> list[Lesson]:
        return await self.repository.list(course_id)

    async def delete(
        self,
        lesson_id: int,
    ) -> None:
        deleted = await self.repository.delete(lesson_id)

        if not deleted:
            raise NotFoundError(
                f"Lesson {lesson_id} not found."
            )


class SectionService:
    def __init__(self, db: AsyncSession):
        self.repository = SectionRepository(db)

    async def create(
        self,
        data: SectionCreate,
    ) -> LessonSection:
        section = await self.repository.create(data)

        if section is None:
            raise ConflictError(
                "Lesson not found or section already exists."
            )

        return section

    async def get(
        self,
        section_id: int,
    ) -> LessonSection:
        section = await self.repository.get(section_id)

        if section is None:
            raise NotFoundError(
                f"Section {section_id} not found."
            )

        return section

    async def list(
        self,
        lesson_id: int,
    ) -> list[LessonSection]:
        return await self.repository.list(lesson_id)

    async def delete(
        self,
        section_id: int,
    ) -> None:
        deleted = await self.repository.delete(section_id)

        if not deleted:
            raise NotFoundError(
                f"Section {section_id} not found."
            )


class VocabularyService:
    def __init__(self, db: AsyncSession):
        self.repository = VocabularyRepository(db)

    async def create(
        self,
        data: VocabularyCreate,
    ) -> Vocabulary:
        vocabulary = await self.repository.create(data)

        if vocabulary is None:
            raise ConflictError(
                "Section not found or vocabulary already exists."
            )

        return vocabulary

    async def get(
        self,
        vocabulary_id: int,
    ) -> Vocabulary:
        vocabulary = await self.repository.get(
            vocabulary_id
        )

        if vocabulary is None:
            raise NotFoundError(
                f"Vocabulary {vocabulary_id} not found."
            )

        return vocabulary

    async def list_by_section(
        self,
        section_id: int,
    ) -> list[Vocabulary]:
        return await self.repository.list_by_section(
            section_id
        )

    async def list_by_course(
        self,
        course_id: int,
    ) -> list[Vocabulary]:
        return await self.repository.list_by_course(
            course_id
        )

    async def list_by_level(
        self,
        language_code: str,
        level: Level,
    ) -> list[Vocabulary]:
        return await self.repository.list_by_level(
            language_code=language_code,
            level=level,
        )

    async def delete(
        self,
        vocabulary_id: int,
    ) -> None:
        deleted = await self.repository.delete(
            vocabulary_id
        )

        if not deleted:
            raise NotFoundError(
                f"Vocabulary {vocabulary_id} not found."
            )
