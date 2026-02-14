import pytest
from pydantic import BaseModel, EmailStr
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import PrivateUsersClient, get_private_users_client
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema


class UsersFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:
        return self.request.email

    @property
    def password(self) -> str:
        return self.request.password

    @property
    def authentication_user(self) -> AuthenticationUserSchema:
        return AuthenticationUserSchema(email=self.email, password=self.password)


@pytest.fixture
def public_users_client() -> PublicUsersClient:
    return get_public_users_client()


@pytest.fixture(scope='function')
def function_create_user(public_users_client: PublicUsersClient) -> UsersFixture:
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)
    return UsersFixture(request=request, response=response)


@pytest.fixture
def private_users_client(function_create_user: UsersFixture) -> PrivateUsersClient:
    request_data = function_create_user.authentication_user
    response = get_private_users_client(request_data)
    return response
