from pydantic import BaseModel, Field, ConfigDict
from tools.fakers import test_data_gen


class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str = Field(default_factory=test_data_gen.sentence)
    course_id: str = Field(alias='courseId', default_factory=test_data_gen.uuid4)
    max_score: int | None = Field(alias='maxScore', default_factory=test_data_gen.max_score)
    min_score: int | None = Field(alias='minScore', default_factory=test_data_gen.min_score)
    order_index: int = Field(alias='orderIndex', default_factory=test_data_gen.integer)
    description: str = Field(default_factory=test_data_gen.text)
    estimated_time: str = Field(alias='estimatedTime', default_factory=test_data_gen.estimated_time)


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на изменение упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None = Field(default_factory=test_data_gen.sentence)
    max_score: int | None = Field(alias='maxScore', default_factory=test_data_gen.max_score)
    min_score: int | None = Field(alias='minScore', default_factory=test_data_gen.min_score)
    order_index: int = Field(alias='orderIndex', default_factory=test_data_gen.integer)
    description: str = Field(default_factory=test_data_gen.text)
    estimated_time: str = Field(alias='estimatedTime', default_factory=test_data_gen.estimated_time)

class ExerciseSchema(BaseModel):
    """
    Описание структуры объекта "Упражнение" (Exercise).
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias='courseId')
    max_score: int | None = Field(alias='maxScore')
    min_score: int | None = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str = Field(alias='estimatedTime')

class ExersiceResponseSchema(BaseModel):
    """
    Описание структуры ответа на запрос об информации о конкретном упражнении.
    """
    exercise: ExerciseSchema

class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа на запрос об информации о списке упражнений.
    """
    exercises: list[ExerciseSchema]