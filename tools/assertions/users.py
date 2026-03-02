from clients.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema, \
    GetUserResponseSchema
from tools.assertions.base import assert_equal
import allure


@allure.step("Check create user response")
def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    assert_equal(actual=response.user.email, expected=request.email, name='email')
    assert_equal(actual=response.user.last_name, expected=request.last_name, name='last_name')
    assert_equal(actual=response.user.first_name, expected=request.first_name, name='first_name')
    assert_equal(actual=response.user.middle_name, expected=request.middle_name, name='middle_name')


@allure.step("Check user")
def assert_user(actual: UserSchema, expected: UserSchema):
    assert_equal(actual=actual.id, expected=expected.id, name='id')
    assert_equal(actual=actual.email, expected=expected.email, name='email')
    assert_equal(actual=actual.first_name, expected=expected.first_name, name='first_name')
    assert_equal(actual=actual.middle_name, expected=expected.middle_name, name='middle_name')
    assert_equal(actual=actual.last_name, expected=expected.last_name, name='last_name')


@allure.step("Check get user response")
def assert_get_user_response(create_user_response: CreateUserResponseSchema, get_user_response: GetUserResponseSchema):
    assert_user(actual=get_user_response, expected=create_user_response)
