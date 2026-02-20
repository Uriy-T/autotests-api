from clients.exercises.exercises_schema import CreateExerciseResponseSchema, CreateExerciseRequestSchema, \
    ExersiceGetByIdResponseSchema, ExerciseSchema
from fixtures.exercises import function_exercise, ExerciseFixture
from tools.assertions.base import assert_equal


def assert_create_exercise_response(actual_exercise_data: CreateExerciseResponseSchema,
                                    expected_exercise_data: CreateExerciseRequestSchema):
    """
    Проверяет что данные введенные при создании упражнения соответствуют данным в теле ответа

    :param actual_exercise_data: данные упражнения, возвращенные запросом
    :param expected_exercise_data: данные упражнения введенные для создания
    :return AssertionError: если хотя бы одно поле не совпадает.
    """
    assert_equal(actual_exercise_data.exercise.title, expected_exercise_data.title, name='title')
    assert_equal(actual_exercise_data.exercise.min_score, expected_exercise_data.min_score, name='min_score')
    assert_equal(actual_exercise_data.exercise.max_score, expected_exercise_data.max_score, name='max_score')
    assert_equal(actual_exercise_data.exercise.order_index, expected_exercise_data.order_index, name='order_index')
    assert_equal(actual_exercise_data.exercise.description, expected_exercise_data.description, name='description')
    assert_equal(actual_exercise_data.exercise.estimated_time, expected_exercise_data.estimated_time,
                 name='estimated_time')

def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверяет, что фактические данные задания соответствуют ожидаемым.

    :param actual: Фактические данные задания.
    :param expected: Ожидаемые данные задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """

    assert_equal(actual.id, expected.id, name='id')
    assert_equal(actual.title, expected.title, name='title')
    assert_equal(actual.course_id, expected.course_id, name='course_id')
    assert_equal(actual.max_score, expected.max_score, name='max_score')
    assert_equal(actual.min_score, expected.min_score, name='min_score')
    assert_equal(actual.order_index, expected.order_index, name='order_index')
    assert_equal(actual.description, expected.description, name='description')
    assert_equal(actual.estimated_time, expected.estimated_time, name='estimated_time')

def assert_get_exercise_response(actual_exercise_data: ExersiceGetByIdResponseSchema, expected_exercise_data: CreateExerciseResponseSchema):
    """
    Проверяет, что ответ на получение задания соответствует ответу на его создание.

    :param actual_exercise_data: Ответ API при запросе данных о задании.
    :param expected_exercise_data: Ответ API при создании задания.
    :raises AssertionError: Если данные файла не совпадают.
    """
    assert_exercise(actual_exercise_data.exercise, expected_exercise_data.exercise)