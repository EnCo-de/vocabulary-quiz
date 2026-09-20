from fastapi import APIRouter

from dependencies import LanguageServiceDep
from schemas import LanguageCreate, LanguageResponse


router = APIRouter()


@router.post(
    "",
    response_model=LanguageResponse,
    status_code=201,
)
async def create_language(
    data: LanguageCreate,
    service: LanguageServiceDep,
):
    return await service.create(data)


@router.get(
    "",
    response_model=list[LanguageResponse],
)
async def list_languages(
    service: LanguageServiceDep,
):
    return await service.list()


@router.get(
    "/code/{code}",
    response_model=LanguageResponse,
)
async def get_language_by_code(
    code: str,
    service: LanguageServiceDep,
):
    return await service.get_by_code(code)


@router.get(
    "/{language_id}",
    response_model=LanguageResponse,
)
async def get_language(
    language_id: int,
    service: LanguageServiceDep,
):
    return await service.get(language_id)


@router.delete(
    "/{language_id}",
    status_code=204,
)
async def delete_language(
    language_id: int,
    service: LanguageServiceDep,
):
    await service.delete(language_id)
