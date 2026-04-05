"""FastAPI backend application"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from schemas import Vocabulary
from repository import get_quiz_words, save_in_dictionary


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # List of allowed origins
    allow_credentials=True,  # Allow cookies and authentication headers
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


@app.get("/")
def index():
    return "Ok"


@app.post("/translation", status_code=201)
def save_translation(translation: Vocabulary) -> Vocabulary:
    result = save_in_dictionary(translation)
    if result is None:
        raise HTTPException(400, "That word exists in the dictionary.")

    return translation


@app.get("/quiz")
def start_quiz(word_count: int | None = None):
    return get_quiz_words(word_count)
