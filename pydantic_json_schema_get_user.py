from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.user_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.fakers import generate_random_email
from tools.assertions.schema import validate_json_schema


public_user_client = get_public_users_client()

new_user_data = CreateUserRequestSchema(
    email=generate_random_email(),
    password='test_password',
    last_name='Семецкий',
    first_name='Петр',
    middle_name='Андреевич'
)

create_new_user_response = public_user_client.create_user(new_user_data)

auth_data = AuthenticationUserSchema(
    email=new_user_data.email,
    password=new_user_data.password
)

private_users_client = get_private_users_client(auth_data)

created_user_data_response = private_users_client.get_user_api(create_new_user_response.user.id)

created_user_data_response_schema = GetUserResponseSchema.model_json_schema()

validate_json_schema(instance=created_user_data_response.json(),
                     schema=created_user_data_response_schema)
