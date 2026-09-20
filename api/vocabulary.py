from typing import Annotated

from fastapi import APIRouter, Query

from dependencies import VocabularyServiceDep
from models import Level
from schemas import VocabularyCreate, VocabularyResponse


router = APIRouter()


@router.post(
    "",
    response_model=VocabularyResponse,
    status_code=201,
)
async def create_vocabulary(
    data: VocabularyCreate,
    service: VocabularyServiceDep,
):
    return await service.create(data)


@router.get(
    "/section/{section_id}",
    response_model=list[VocabularyResponse],
)
async def list_section_vocabulary(
    section_id: int,
    service: VocabularyServiceDep,
):
    return await service.list_by_section(section_id)


@router.get(
    "/course/{course_id}",
    response_model=list[VocabularyResponse],
)
async def list_course_vocabulary(
    course_id: int,
    service: VocabularyServiceDep,
):
    return await service.list_by_course(course_id)


@router.get(
    "/level/{language_code}",
    response_model=list[VocabularyResponse],
)
async def list_level_vocabulary(
    language_code: str,
    level: Annotated[Level, Query()],
    service: VocabularyServiceDep,
):
    return await service.list_by_level(
        language_code=language_code,
        level=level,
    )


@router.get(
    "/{vocabulary_id}",
    response_model=VocabularyResponse,
)
async def get_vocabulary(
    vocabulary_id: int,
    service: VocabularyServiceDep,
):
    return await service.get(vocabulary_id)


@router.delete(
    "/{vocabulary_id}",
    status_code=204,
)
async def delete_vocabulary(
    vocabulary_id: int,
    service: VocabularyServiceDep,
):
    await service.delete(vocabulary_id)
