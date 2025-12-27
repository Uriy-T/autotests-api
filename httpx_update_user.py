import httpx

from tools.fakers import generate_random_email

create_user_payload = {
    'email': generate_random_email(),
    "password": "test_password",
    "lastName": "Жуков",
    "firstName": "Клим",
    "middleName": "Александрович"
}

create_user_response = httpx.post('http://localhost:8000/api/v1/users', json=create_user_payload)
create_user_response_data = create_user_response.json()

print(create_user_response.status_code)
print(create_user_response.json())

auth_data_payload = {
    'email': create_user_payload['email'],
    'password': create_user_payload['password']
}
auth_response = httpx.post('http://127.0.0.1:8000/api/v1/authentication/login', json=auth_data_payload)
auth_response_data = auth_response.json()

print(auth_response.status_code)
print(auth_response_data)

patch_headers = {'Authorization': f"Bearer {auth_response_data['token']['accessToken']}"}

patch_payload = {
    "email": generate_random_email(),
    "lastName": "Пушкин",
    "firstName": "Александр",
    "middleName": "Сергеевич"
}

patch_user_request = httpx.patch(f'http://127.0.0.1:8000/api/v1/users/{create_user_response_data["user"]["id"]}',
                                 headers=patch_headers, json=patch_payload)
patch_user_request_data = patch_user_request.json()

print(patch_user_request.status_code)
print(patch_user_request_data)
