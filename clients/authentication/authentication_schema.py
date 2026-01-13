from pydantic import BaseModel, Field, EmailStr


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
    email: EmailStr
    password: str


class RefreshRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление токена
    """
    refresh_token: str = Field(alias='refreshToken')