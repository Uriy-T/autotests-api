from pydantic import BaseModel, Field, EmailStr, ConfigDict
from tools.fakers import test_data_gen

class UserSchema(BaseModel):
    """
    Описание структуры пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')


class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr = Field(default_factory=test_data_gen.email)
    password: str = Field(default_factory=test_data_gen.password)
    last_name: str = Field(alias='lastName', default_factory=test_data_gen.last_name)
    first_name: str = Field(alias='firstName', default_factory=test_data_gen.first_name)
    middle_name: str = Field(alias='middleName', default_factory=test_data_gen.middle_name)


class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя.
    """
    user: UserSchema


class UpdateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr | None = Field(default_factory=test_data_gen.email)
    last_name: str | None = Field(alias='lastName', default_factory=test_data_gen.last_name)
    first_name: str | None = Field(alias='firstName', default_factory=test_data_gen.first_name)
    middle_name: str | None = Field(alias='middleName', default_factory=test_data_gen.middle_name)


class UpdateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа обновления пользователя.
    """
    user: UserSchema


class GetUserResponseSchema(BaseModel):
    """
    Описание структуры ответа получения пользователя.
    """
    user: UserSchema
