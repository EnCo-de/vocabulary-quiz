# Vocabulary-quiz
Vocabulary quiz built with FastAPI

For a small project, start with

```
app/
├── main.py
├── database.py
├── dependencies.py
├── exceptions.py
├── models.py
├── schemas.py
├── repository.py
├── services.py
└── api/
    ├── __init__.py
    ├── languages.py
    ├── courses.py
    ├── lessons.py
    ├── sections.py
    └── vocabulary.py
```

The FastAPI + SQLAlchemy async vocabulary app project structure separated into a few distinct layers.

```
app/
├── main.py
│
├── database.py
├── models.py
│
├── schemas/
│   ├── __init__.py
│   ├── language.py
│   ├── course.py
│   ├── lesson.py
│   ├── vocabulary.py
│   └── common.py
│
├── repositories/
│   ├── __init__.py
│   ├── languages.py
│   ├── courses.py
│   ├── lessons.py
│   └── vocabulary.py
│
├── services/
│   ├── __init__.py
│   ├── courses.py
│   └── quiz.py
│
├── api/
│   ├── __init__.py
│   ├── languages.py
│   ├── courses.py
│   ├── lessons.py
│   ├── vocabulary.py
│   └── quiz.py
│
└── migrations/
```

One thing, the Base.metadata.create_all() is convenient while developing, but once the schema is established, the next step should be Alembic migrations so database changes are versioned rather than recreated implicitly.

```
POST   /languages
GET    /languages
GET    /languages/{id}
GET    /languages/code/{code}
DELETE /languages/{id}

POST   /courses
GET    /courses?language=es&level=B1
GET    /courses/{id}
DELETE /courses/{id}

POST   /lessons
GET    /lessons/{id}
GET    /lessons/course/{course_id}
DELETE /lessons/{id}

POST   /sections
GET    /sections/{id}
GET    /sections/lesson/{lesson_id}
DELETE /sections/{id}

POST   /vocabulary
GET    /vocabulary/{id}
GET    /vocabulary/section/{section_id}
GET    /vocabulary/course/{course_id}
GET    /vocabulary/level/{language_code}?level=B1
DELETE /vocabulary/{id}
```
One adjustment to route ordering. In vocabulary.py, fixed paths such as `/section/{section_id}` should be defined before `/{vocabulary_id}`. Otherwise FastAPI can interpret "section" as the `vocabulary_id` path parameter. The same principle applies to the other routers.

1. exceptions.py                    ✓
2. repository classes               ✓
3. service classes                  ✓
4. response schemas                 ✓
5. API routers                      ✓
6. main.py router registration      ✓
7. database initialization
8. Alembic migrations
9. tests
10. quiz/review business logic
