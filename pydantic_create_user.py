from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    """
    Базовая модель описания пользователя.
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')


class CreateUserRequestSchema(BaseModel):
    """
    Модель описания тела запроса на создание пользователя
    """
    email: EmailStr
    password: str
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')


class CreateUserResponseSchema(BaseModel):
    """
    Модель описания успешного ответа от сервера по итогу создания пользователя: статус-код == 200
    """
    user: UserSchema
