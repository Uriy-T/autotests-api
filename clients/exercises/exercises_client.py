from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, UpdateExerciseRequestSchema, CreateExerciseResponseSchema, GetExercisesResponseSchema


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
        return self.get(f'/api/v1/exercises?courseId={courseid}')

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения информации о конкретном упражнении по его uuid.

        :param exercise_id: идентификатор упражнения в uuid формате.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f'/api/v1/exercises/{exercise_id}')

    def create_exercise_api(self, exercise_data: CreateExerciseRequestSchema):
        """
        Метод создания упражнения.

        :param exercise_data: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/exercises', json=exercise_data.model_dump(by_alias=True))

    def update_exercise_api(self, exercise_id: str, data_for_update: UpdateExerciseRequestSchema) -> Response:
        """
        Метод изменения упражнения по его uuid.

        :param exercise_id: идентификатор упражнения в uuid формате.
        :param data_for_update: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
                """
        return self.patch(f'/api/v1/exercises/{exercise_id}', json=data_for_update.model_dump(by_alias=True))

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления конкретного упражнения по его uuid.

        :param exercise_id: идентификатор упражнения в uuid формате.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f'/api/v1/exercises/{exercise_id}')

    def get_exercise(self, exercise_id: str) -> CreateExerciseResponseSchema:
        response = self.get_exercise_api(exercise_id)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def get_exercises(self, courseid: str) -> GetExercisesResponseSchema:
        response = self.get_exercises_api(courseid)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(self, exercise_data: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        response = self.create_exercise_api(exercise_data)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, data_for_update: UpdateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        response = self.update_exercise_api(exercise_id, data_for_update)
        return CreateExerciseResponseSchema.model_validate_json(response.text)


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
