from http import HTTPStatus
import pytest
from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from tests.conftest import UsersFixture
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.authentication
def test_login(function_create_user: UsersFixture, authentication_client: AuthenticationClient):
    request_data = LoginRequestSchema(
        email=function_create_user.email,
        password=function_create_user.password
    )

    request = authentication_client.login_api(request_data)
    response = LoginResponseSchema.model_validate_json(request.text)

    assert_status_code(request.status_code, HTTPStatus.OK)
    assert_login_response(response)
    validate_json_schema(instance=request.json(), schema=response.model_json_schema())
