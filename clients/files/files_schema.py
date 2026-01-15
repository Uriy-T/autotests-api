from pydantic import BaseModel, HttpUrl, Field
from tools.fakers import test_data_gen


class FileSchema(BaseModel):
    """
    Описание объекта File.
    """
    id: str
    filename: str
    directory: str
    url: HttpUrl


class CreateFileResponseSchema(BaseModel):
    """
    Описание структуры ответа объекта "Файл"
    """
    file: FileSchema


class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """
    filename: str = Field(default_factory=lambda: f'{test_data_gen.uuid4()}.png')
    directory: str = Field(default='tests')
    upload_file: str