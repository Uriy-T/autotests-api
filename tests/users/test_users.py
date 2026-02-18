from http import HTTPStatus
import pytest
from tools.fakers import test_data_gen
from clients.users.private_users_client import PrivateUsersClient
from clients.users.public_users_client import PublicUsersClient
from clients.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from fixtures.users import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response, assert_get_user_response


@pytest.mark.users
@pytest.mark.regression
class TestUsers:
    @pytest.mark.parametrize('domain', ['mail.ru', 'gmail.com', 'example.com'])
    def test_create_user(self, domain: str, public_users_client: PublicUsersClient):
        user_create_request_data = CreateUserRequestSchema(
            email=test_data_gen.email(domain)
        )
        response = public_users_client.create_user_api(user_create_request_data)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_user_response(user_create_request_data, response_data)

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())


    def test_get_user_me(self, function_user: UserFixture, private_users_client: PrivateUsersClient):
        create_user_response = function_user.response
        response = private_users_client.get_user_me_api()
        response_data = GetUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_user_response(create_user_response=create_user_response.user, get_user_response=response_data.user)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
