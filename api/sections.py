from fastapi import APIRouter

from dependencies import SectionServiceDep
from schemas import SectionCreate, SectionResponse


router = APIRouter()


@router.post(
    "",
    response_model=SectionResponse,
    status_code=201,
)
async def create_section(
    data: SectionCreate,
    service: SectionServiceDep,
):
    return await service.create(data)


@router.get(
    "/lesson/{lesson_id}",
    response_model=list[SectionResponse],
)
async def list_sections(
    lesson_id: int,
    service: SectionServiceDep,
):
    return await service.list(lesson_id)


@router.get(
    "/{section_id}",
    response_model=SectionResponse,
)
async def get_section(
    section_id: int,
    service: SectionServiceDep,
):
    return await service.get(section_id)


@router.delete(
    "/{section_id}",
    status_code=204,
)
async def delete_section(
    section_id: int,
    service: SectionServiceDep,
):
    await service.delete(section_id)
