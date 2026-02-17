from pydantic import BaseModel

from clients.exercises.exercises_client import ExercisesClient, get_exercises_client
import pytest

from clients.exercises.exercises_schema import CreateExerciseRequestSchema, ExersiceResponseSchema
from fixtures.courses import CoursesFixture
from fixtures.users import UserFixture


class ExerciseFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: ExersiceResponseSchema


@pytest.fixture(scope='function')
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(function_user.authentication_user)


@pytest.fixture(scope='function')
def function_exercise(exercises_client: ExercisesClient,
                      function_course: CoursesFixture) -> ExerciseFixture:
    request_data = CreateExerciseRequestSchema(
        courseId=function_course.response.course.id
    )
    response_data = exercises_client.create_exercise(request_data)
    return ExerciseFixture(request=request_data, response=response_data)
