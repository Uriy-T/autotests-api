from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.user_schema import CreateUserRequestSchema
from tools.fakers import generate_random_email

public_user_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=generate_random_email(),
    password='test_password',
    last_name='string',
    first_name='string',
    middle_name='string'
)

create_user_response = public_user_client.create_user(create_user_request)
print('Create user data:', create_user_response)

authentication_user_dict = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

private_users_client = get_private_users_client(authentication_user_dict)

get_user_response = private_users_client.get_user(create_user_response.user.id)
print('Get user data:', get_user_response)
