"""FastAPI backend application"""

from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from api import (
    courses,
    languages,
    lessons,
    sections,
    vocabulary,
)
from database import engine
from exceptions import ConflictError, NotFoundError
from models import Base
from schemas import VocabularyCreate, VocabularyResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Development only.
    #
    # In production, use Alembic migrations instead of
    # Base.metadata.create_all().
    async with engine.begin() as connection:
        await connection.run_sync(
            Base.metadata.create_all
        )

    yield

    await engine.dispose()


app = FastAPI(
    title="Vocabulary API",
    lifespan=lifespan,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # List of allowed origins
    allow_credentials=True,  # Allow cookies and authentication headers
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


@app.exception_handler(NotFoundError)
async def not_found_handler(
    request: Request,
    exc: NotFoundError,
):
    return JSONResponse(
        status_code=404,
        content={
            "detail": exc.message,
        },
    )


@app.exception_handler(ConflictError)
async def conflict_handler(
    request: Request,
    exc: ConflictError,
):
    return JSONResponse(
        status_code=409,
        content={
            "detail": exc.message,
        },
    )


app.include_router(
    languages.router,
    prefix="/languages",
    tags=["Languages"],
)

app.include_router(
    courses.router,
    prefix="/courses",
    tags=["Courses"],
)

app.include_router(
    lessons.router,
    prefix="/lessons",
    tags=["Lessons"],
)

app.include_router(
    sections.router,
    prefix="/sections",
    tags=["Sections"],
)

app.include_router(
    vocabulary.router,
    prefix="/vocabulary",
    tags=["Vocabulary"],
)


@app.get("/")
async def index():
    return {"status": "ok"}


@app.post("/translation", status_code=201, response_model=VocabularyResponse)
async def save_translation(translation: VocabularyCreate) -> VocabularyResponse:
    return translation


@app.get("/quiz")
def start_quiz(word_count: int | None = None) -> list[tuple[str, str]]:
    import random

    store = {
        "uno": "one",
        "dos": "two",
        "tres": "three",
        "cuatro": "four",
        "cinco": "five",
        "seis": "six",
        "siete": "seven",
        "ocho": "eight",
        "nueve": "nine",
        "diez": "ten",
        "once": "eleven",
        "doce": "twelve",
    }

    return random.sample(sorted(store.items()), word_count or 5)
