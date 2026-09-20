from typing import Annotated

from fastapi import APIRouter, Query

from dependencies import CourseServiceDep
from models import Level
from schemas import CourseCreate, CourseResponse


router = APIRouter()


@router.post(
    "",
    response_model=CourseResponse,
    status_code=201,
)
async def create_course(
    data: CourseCreate,
    service: CourseServiceDep,
):
    return await service.create(data)


@router.get(
    "",
    response_model=list[CourseResponse],
)
async def list_courses(
    language: Annotated[
        str,
        Query(
            min_length=2,
            max_length=10,
        ),
    ],
    level: Level,
    service: CourseServiceDep,
):
    return await service.list(
        language_code=language,
        level=level,
    )


@router.get(
    "/{course_id}",
    response_model=CourseResponse,
)
async def get_course(
    course_id: int,
    service: CourseServiceDep,
):
    return await service.get(course_id)


@router.delete(
    "/{course_id}",
    status_code=204,
)
async def delete_course(
    course_id: int,
    service: CourseServiceDep,
):
    await service.delete(course_id)
