from httpx import Response
import allure
from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, UpdateExerciseRequestSchema, CreateExerciseResponseSchema, GetExercisesResponseSchema
from tools.routes import APIRoutes
from clients.api_coverage import tracker

class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    @allure.step('Get list of exercises')
    @tracker.track_coverage_httpx(f'{APIRoutes.EXERCISES}?courseId={{courseid}}')
    def get_exercises_api(self, courseid: str) -> Response:
        """
        Метод получения списка упражнений по uuid курса.

        :param courseid: идентификатор курса в uuid формате.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f'{APIRoutes.EXERCISES}?courseId={courseid}')

    @allure.step('Get list of exercise by id')
    @tracker.track_coverage_httpx(f'{APIRoutes.EXERCISES}/{{exercise_id}}')
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения информации о конкретном упражнении по его uuid.

        :param exercise_id: идентификатор упражнения в uuid формате.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f'{APIRoutes.EXERCISES}/{exercise_id}')

    @allure.step('Create exercise')
    @tracker.track_coverage_httpx(f'{APIRoutes.EXERCISES}')
    def create_exercise_api(self, exercise_data: CreateExerciseRequestSchema):
        """
        Метод создания упражнения.

        :param exercise_data: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(APIRoutes.EXERCISES, json=exercise_data.model_dump(by_alias=True))

    @allure.step('Create exercise')
    @tracker.track_coverage_httpx(f'{APIRoutes.EXERCISES}/{{exercise_id}}')
    def update_exercise_api(self, exercise_id: str, data_for_update: UpdateExerciseRequestSchema) -> Response:
        """
        Метод изменения упражнения по его uuid.

        :param exercise_id: идентификатор упражнения в uuid формате.
        :param data_for_update: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
                """
        return self.patch(f'{APIRoutes.EXERCISES}/{exercise_id}', json=data_for_update.model_dump(by_alias=True))

    @allure.step('Delete exercise')
    @tracker.track_coverage_httpx(f'{APIRoutes.EXERCISES}/{{exercise_id}}')
    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления конкретного упражнения по его uuid.

        :param exercise_id: идентификатор упражнения в uuid формате.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f'{APIRoutes.EXERCISES}/{exercise_id}')

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
