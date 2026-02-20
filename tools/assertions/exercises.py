from clients.exercises.exercises_schema import ExersiceCreateResponseSchema, CreateExerciseRequestSchema
from tools.assertions.base import assert_equal


def assert_create_exercise_response(actual_exercise_data: ExersiceCreateResponseSchema,
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
