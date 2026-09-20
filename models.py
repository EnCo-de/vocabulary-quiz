from enum import StrEnum

from sqlalchemy import Enum, ForeignKey, String, Text, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Level(StrEnum):
    A1 = "A1"
    A2 = "A2"
    B1 = "B1"
    B2 = "B2"
    C1 = "C1"
    C2 = "C2"


class Language(Base):
    __tablename__ = "languages"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    code: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
        unique=True,
    )

    courses: Mapped[list["Course"]] = relationship(
        back_populates="language",
        cascade="all, delete-orphan",
    )


class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    level: Mapped[Level] = mapped_column(
        Enum(
            Level,
            native_enum=False,
            values_callable=lambda enum: [item.value for item in enum],
        ),
        nullable=False,
    )

    language_id: Mapped[int] = mapped_column(
        ForeignKey("languages.id"),
        nullable=False,
        index=True,
    )

    language: Mapped["Language"] = relationship(
        back_populates="courses",
    )

    lessons: Mapped[list["Lesson"]] = relationship(
        back_populates="course",
        cascade="all, delete-orphan",
        order_by="Lesson.position",
    )

    __table_args__ = (
        UniqueConstraint(
            "language_id",
            "level",
            "title",
            name="uq_course_language_level_title",
        ),
    )


class Lesson(Base):
    __tablename__ = "lessons"

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    position: Mapped[int] = mapped_column(
        nullable=False,
        default=0,
    )

    course_id: Mapped[int] = mapped_column(
        ForeignKey("courses.id"),
        nullable=False,
        index=True,
    )

    course: Mapped["Course"] = relationship(
        back_populates="lessons",
    )

    sections: Mapped[list["LessonSection"]] = relationship(
        back_populates="lesson",
        cascade="all, delete-orphan",
        order_by="LessonSection.position",
    )

    __table_args__ = (
        UniqueConstraint(
            "course_id",
            "title",
            name="uq_lesson_course_title",
        ),
    )


class LessonSection(Base):
    __tablename__ = "lesson_sections"

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    position: Mapped[int] = mapped_column(
        nullable=False,
        default=0,
    )

    lesson_id: Mapped[int] = mapped_column(
        ForeignKey("lessons.id"),
        nullable=False,
        index=True,
    )

    lesson: Mapped["Lesson"] = relationship(
        back_populates="sections",
    )

    vocabulary: Mapped[list["Vocabulary"]] = relationship(
        back_populates="section",
        cascade="all, delete-orphan",
        order_by="Vocabulary.id",
    )

    __table_args__ = (
        UniqueConstraint(
            "lesson_id",
            "title",
            name="uq_section_lesson_title",
        ),
    )


class Vocabulary(Base):
    __tablename__ = "vocabulary"

    id: Mapped[int] = mapped_column(primary_key=True)

    word: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    translation: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    section_id: Mapped[int] = mapped_column(
        ForeignKey("lesson_sections.id"),
        nullable=False,
        index=True,
    )

    section: Mapped["LessonSection"] = relationship(
        back_populates="vocabulary",
    )

    __table_args__ = (
        UniqueConstraint(
            "section_id",
            "word",
            name="uq_vocabulary_section_word",
        ),
    )
