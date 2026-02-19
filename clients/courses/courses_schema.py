from pydantic import BaseModel, Field, ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.user_schema import UserSchema
from tools.fakers import test_data_gen


class CourseSchema(BaseModel):
    """
    Описание структуры объекта Course.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    description: str
    preview_file: FileSchema = Field(alias='previewFile')
    estimated_time: str = Field(alias='estimatedTime')
    created_by_user: UserSchema = Field(alias='createdByUser')


class CreateCourseResponseSchema(BaseModel):
    course: CourseSchema


class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    model_config = ConfigDict(populate_by_name=True)
    user_id: str = Field(alias='userId')


class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str = Field(default_factory=test_data_gen.sentence)
    max_score: int = Field(alias='maxScore', default_factory=test_data_gen.max_score)
    min_score: int = Field(alias='minScore', default_factory=test_data_gen.min_score)
    description: str = Field(default_factory=test_data_gen.text)
    estimated_time: str = Field(alias='estimatedTime', default_factory=test_data_gen.estimated_time)
    preview_file_id: str = Field(alias='previewFileId', default_factory=test_data_gen.uuid4)
    created_by_user_id: str = Field(alias='createdByUserId', default_factory=test_data_gen.uuid4)


class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None = Field(default_factory=test_data_gen.sentence)
    max_score: int | None = Field(alias='maxScore', default_factory=test_data_gen.max_score)
    min_score: int | None = Field(alias='minScore', default_factory=test_data_gen.min_score)
    description: str | None = Field(default_factory=test_data_gen.text)
    estimated_time: str = Field(alias='estimatedTime', default_factory=test_data_gen.estimated_time)


class UpdateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа обновления курса.
    """
    course: CourseSchema


class GetCoursesResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение списка курсов.
    """
    courses: list[CourseSchema]
