from pydantic import BaseModel, Field, ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.user_schema import UserSchema

class ExerciseCreateRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias='courseId')
    max_score: int | None = Field(alias='maxScore')
    min_score: int | None = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str = Field(alias='estimatedTime')


class ExerciseUpdateRequestSchema(BaseModel):
    """
    Описание структуры запроса на изменение упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: int | None = Field(alias='maxScore')
    min_score: int | None = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str | None
    estimated_time: str = Field(alias='estimatedTime')

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