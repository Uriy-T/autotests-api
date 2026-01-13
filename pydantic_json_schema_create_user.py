from clients.users.public_users_client import get_public_users_client
from clients.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.fakers import generate_random_email
from tools.assertions.schema import validate_json_schema

public_user_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=generate_random_email(),
    password='test_password',
    last_name='string',
    first_name='string',
    middle_name='string'
)

create_user_response = public_user_client.create_user_api(create_user_request)
create_user_response_json = create_user_response.json()
create_user_response_schema = CreateUserResponseSchema.model_json_schema()

validate_json_schema(schema=create_user_response_schema, instance=create_user_response_json)
