from httpx import Response

from clients.api_client import APIClient
from typing import TypedDict

from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class ExerciseCreateRequest(TypedDict):
    """
    Описание структуры запроса на создание упражнения.
    """
    title: str
    courseId: str
    maxScore: int | None
    minScore: int | None
    orderIndex: int
    description: str
    estimatedTime: str


class ExerciseUpdateRequest(TypedDict):
    """
    Описание структуры запроса на изменение упражнения.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class Exercise(TypedDict):
    """
    Описание структуры упражнения.
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class ExersiceResponseDict(TypedDict):
    """
    Описание структуры запроса на информацию о конкретном упражнении.
    """
    exercise: Exercise

class GetExercisesResponseDict(TypedDict):
    exercises: list[Exercise]


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, courseid: str) -> Response:
        """
        Метод получения списка упражнений по uuid курса.

        :param courseid: идентификатор курса в uuid формате.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f'/api/v1/exercises/{courseid}')

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения информации о конкретном упражнении по его uuid.

        :param exercise_id: идентификатор упражнения в uuid формате.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f'/api/v1/exercises/{exercise_id}')

    def create_exercise_api(self, exercise_data: ExerciseCreateRequest):
        """
        Метод создания упражнения.

        :param exercise_data: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/exercises', json=exercise_data)

    def update_exercise_api(self, exercise_id: str, data_for_update: ExerciseUpdateRequest) -> Response:
        """
        Метод изменения упражнения по его uuid.

        :param exercise_id: идентификатор упражнения в uuid формате.
        :param data_for_update: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
                """
        return self.patch(f'/api/v1/exercises/{exercise_id}', json=data_for_update)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления конкретного упражнения по его uuid.

        :param exercise_id: идентификатор упражнения в uuid формате.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f'/api/v1/exercises/{exercise_id}')

    def get_exercise(self, exercise_id: str) -> ExersiceResponseDict:
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def get_exercises(self, courseid: str) -> GetExercisesResponseDict:
        response = self.get_exercises_api(courseid)
        return response.json()

    def create_exercise(self, exercise_data: ExerciseCreateRequest) -> ExersiceResponseDict:
        response = self.create_exercise_api(exercise_data)
        return response.json()

    def update_exercise(self, exercise_id: str, data_for_update: ExerciseUpdateRequest) -> ExersiceResponseDict:
        response = self.update_exercise_api(exercise_id, data_for_update)
        return response.json()


def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
