from fastapi import APIRouter

from dependencies import LessonServiceDep
from schemas import LessonCreate, LessonResponse


router = APIRouter()


@router.post(
    "",
    response_model=LessonResponse,
    status_code=201,
)
async def create_lesson(
    data: LessonCreate,
    service: LessonServiceDep,
):
    return await service.create(data)


@router.get(
    "/course/{course_id}",
    response_model=list[LessonResponse],
)
async def list_lessons(
    course_id: int,
    service: LessonServiceDep,
):
    return await service.list(course_id)


@router.get(
    "/{lesson_id}",
    response_model=LessonResponse,
)
async def get_lesson(
    lesson_id: int,
    service: LessonServiceDep,
):
    return await service.get(lesson_id)


@router.delete(
    "/{lesson_id}",
    status_code=204,
)
async def delete_lesson(
    lesson_id: int,
    service: LessonServiceDep,
):
    await service.delete(lesson_id)
