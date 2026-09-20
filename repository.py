"""Save words in the dictionary"""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from models import (
    Course,
    Language,
    Level,
    Lesson,
    LessonSection,
    Vocabulary,
)
from schemas import (
    CourseCreate,
    LanguageCreate,
    LessonCreate,
    SectionCreate,
    VocabularyCreate,
)


class LanguageRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(
        self,
        data: LanguageCreate,
    ) -> Language | None:
        result = await self.db.execute(
            select(Language).where(
                Language.code == data.code
            )
        )

        if result.scalar_one_or_none() is not None:
            return None

        language = Language(
            name=data.name,
            code=data.code,
        )

        self.db.add(language)

        await self.db.commit()
        await self.db.refresh(language)

        return language

    async def get(
        self,
        language_id: int,
    ) -> Language | None:
        return await self.db.get(Language, language_id)

    async def get_by_code(
        self,
        code: str,
    ) -> Language | None:
        result = await self.db.execute(
            select(Language).where(
                Language.code == code
            )
        )

        return result.scalar_one_or_none()

    async def list(self) -> list[Language]:
        result = await self.db.execute(
            select(Language).order_by(Language.name)
        )

        return list(result.scalars().all())

    async def delete(
        self,
        language_id: int,
    ) -> bool:
        language = await self.get(language_id)

        if language is None:
            return False

        await self.db.delete(language)
        await self.db.commit()

        return True


class CourseRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(
        self,
        data: CourseCreate,
    ) -> Course | None:
        language = await self.db.get(
            Language,
            data.language_id,
        )

        if language is None:
            return None

        result = await self.db.execute(
            select(Course).where(
                Course.language_id == data.language_id,
                Course.level == data.level,
                Course.title == data.title,
            )
        )

        if result.scalar_one_or_none() is not None:
            return None

        course = Course(
            title=data.title,
            description=data.description,
            level=data.level,
            language_id=data.language_id,
        )

        self.db.add(course)

        await self.db.commit()
        await self.db.refresh(course)

        return course

    async def get(
        self,
        course_id: int,
    ) -> Course | None:
        result = await self.db.execute(
            select(Course)
            .where(Course.id == course_id)
            .options(
                selectinload(Course.language),
                selectinload(Course.lessons),
            )
        )

        return result.scalar_one_or_none()

    async def list(
        self,
        language_code: str,
        level: Level,
    ) -> list[Course]:
        result = await self.db.execute(
            select(Course)
            .join(Course.language)
            .where(
                Language.code == language_code,
                Course.level == level,
            )
            .order_by(Course.id)
        )

        return list(result.scalars().all())

    async def list_all(self) -> list[Course]:
        result = await self.db.execute(
            select(Course)
            .options(
                selectinload(Course.language),
            )
            .order_by(Course.id)
        )

        return list(result.scalars().all())

    async def delete(
        self,
        course_id: int,
    ) -> bool:
        course = await self.db.get(Course, course_id)

        if course is None:
            return False

        await self.db.delete(course)
        await self.db.commit()

        return True


class LessonRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(
        self,
        data: LessonCreate,
    ) -> Lesson | None:
        course = await self.db.get(
            Course,
            data.course_id,
        )

        if course is None:
            return None

        result = await self.db.execute(
            select(Lesson).where(
                Lesson.course_id == data.course_id,
                Lesson.title == data.title,
            )
        )

        if result.scalar_one_or_none() is not None:
            return None

        lesson = Lesson(
            title=data.title,
            description=data.description,
            position=data.position,
            course_id=data.course_id,
        )

        self.db.add(lesson)

        await self.db.commit()
        await self.db.refresh(lesson)

        return lesson

    async def get(
        self,
        lesson_id: int,
    ) -> Lesson | None:
        result = await self.db.execute(
            select(Lesson)
            .where(Lesson.id == lesson_id)
            .options(
                selectinload(Lesson.sections),
            )
        )

        return result.scalar_one_or_none()

    async def list(
        self,
        course_id: int,
    ) -> list[Lesson]:
        result = await self.db.execute(
            select(Lesson)
            .where(Lesson.course_id == course_id)
            .order_by(Lesson.position)
        )

        return list(result.scalars().all())

    async def delete(
        self,
        lesson_id: int,
    ) -> bool:
        lesson = await self.db.get(Lesson, lesson_id)

        if lesson is None:
            return False

        await self.db.delete(lesson)
        await self.db.commit()

        return True


class SectionRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(
        self,
        data: SectionCreate,
    ) -> LessonSection | None:
        lesson = await self.db.get(
            Lesson,
            data.lesson_id,
        )

        if lesson is None:
            return None

        result = await self.db.execute(
            select(LessonSection).where(
                LessonSection.lesson_id == data.lesson_id,
                LessonSection.title == data.title,
            )
        )

        if result.scalar_one_or_none() is not None:
            return None

        section = LessonSection(
            title=data.title,
            position=data.position,
            lesson_id=data.lesson_id,
        )

        self.db.add(section)

        await self.db.commit()
        await self.db.refresh(section)

        return section

    async def get(
        self,
        section_id: int,
    ) -> LessonSection | None:
        result = await self.db.execute(
            select(LessonSection)
            .where(LessonSection.id == section_id)
            .options(
                selectinload(LessonSection.vocabulary),
            )
        )

        return result.scalar_one_or_none()

    async def list(
        self,
        lesson_id: int,
    ) -> list[LessonSection]:
        result = await self.db.execute(
            select(LessonSection)
            .where(
                LessonSection.lesson_id == lesson_id
            )
            .order_by(LessonSection.position)
        )

        return list(result.scalars().all())

    async def delete(
        self,
        section_id: int,
    ) -> bool:
        section = await self.db.get(
            LessonSection,
            section_id,
        )

        if section is None:
            return False

        await self.db.delete(section)
        await self.db.commit()

        return True


class VocabularyRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(
        self,
        data: VocabularyCreate,
    ) -> Vocabulary | None:
        section = await self.db.get(
            LessonSection,
            data.section_id,
        )

        if section is None:
            return None

        result = await self.db.execute(
            select(Vocabulary).where(
                Vocabulary.section_id == data.section_id,
                Vocabulary.word == data.word,
            )
        )

        if result.scalar_one_or_none() is not None:
            return None

        vocabulary = Vocabulary(
            word=data.word,
            translation=data.translation,
            section_id=data.section_id,
        )

        self.db.add(vocabulary)

        await self.db.commit()
        await self.db.refresh(vocabulary)

        return vocabulary

    async def get(
        self,
        vocabulary_id: int,
    ) -> Vocabulary | None:
        return await self.db.get(
            Vocabulary,
            vocabulary_id,
        )

    async def list_by_section(
        self,
        section_id: int,
    ) -> list[Vocabulary]:
        result = await self.db.execute(
            select(Vocabulary)
            .where(
                Vocabulary.section_id == section_id
            )
            .order_by(Vocabulary.id)
        )

        return list(result.scalars().all())

    async def list_by_course(
        self,
        course_id: int,
    ) -> list[Vocabulary]:
        result = await self.db.execute(
            select(Vocabulary)
            .join(Vocabulary.section)
            .join(LessonSection.lesson)
            .where(
                Lesson.course_id == course_id
            )
            .order_by(
                Lesson.position,
                LessonSection.position,
                Vocabulary.id,
            )
        )

        return list(result.scalars().all())

    async def list_by_level(
        self,
        language_code: str,
        level: Level,
    ) -> list[Vocabulary]:
        result = await self.db.execute(
            select(Vocabulary)
            .join(Vocabulary.section)
            .join(LessonSection.lesson)
            .join(Lesson.course)
            .join(Course.language)
            .where(
                Language.code == language_code,
                Course.level == level,
            )
            .order_by(
                Course.id,
                Lesson.position,
                LessonSection.position,
                Vocabulary.id,
            )
        )

        return list(result.scalars().all())

    async def delete(
        self,
        vocabulary_id: int,
    ) -> bool:
        vocabulary = await self.db.get(
            Vocabulary,
            vocabulary_id,
        )

        if vocabulary is None:
            return False

        await self.db.delete(vocabulary)
        await self.db.commit()

        return True
