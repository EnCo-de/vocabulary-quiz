# Vocabulary-quiz
Vocabulary quiz built with FastAPI

For a small project, start with

```
app/
├── main.py
├── schemas.py
├── services.py
├── repository.py
├── models.py
├── database.py
└── api/
    ├── courses.py
    ├── lessons.py
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
