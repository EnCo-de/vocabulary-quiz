"""Save words in the dictionary"""

import random

from schemas import Vocabulary

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


def get_quiz_words(n: int | None = None):
    return random.sample(sorted(store.items()), n or 3)


def save_in_dictionary(translation: Vocabulary) -> Vocabulary | None:
    if store.get(translation.word):
        return None

    store[translation.word] = translation.translation
    return translation
