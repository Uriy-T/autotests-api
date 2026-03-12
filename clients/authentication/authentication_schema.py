from pydantic import BaseModel, Field, EmailStr
from tools.fakers import test_data_gen


class TokenSchema(BaseModel):
    """
    Описание структуры описания набора токенов
    """
    token_type: str = Field(alias='tokenType')
    access_token: str = Field(alias='accessToken')
    refresh_token: str = Field(alias='refreshToken')


class LoginResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение набора токенов
    """
    token: TokenSchema


class LoginRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление токена
    """
    email: EmailStr = Field(default_factory=test_data_gen.email)
    password: str = Field(default_factory=test_data_gen.password)


class RefreshRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление токена
    """
    refresh_token: str = Field(alias='refreshToken', default_factory=test_data_gen.sentence)