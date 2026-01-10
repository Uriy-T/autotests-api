from pydantic import BaseModel, HttpUrl


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
    filename: str
    directory: str
    upload_file: str
