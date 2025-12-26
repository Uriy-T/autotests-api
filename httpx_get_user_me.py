import httpx

auth_data = {
    'email': 'user@example.com',
    'password': 'test_pass'
}
auth_request = httpx.post('http://127.0.0.1:8000/api/v1/authentication/login', json=auth_data)
token_set = auth_request.json()

print(auth_request.status_code)
print(token_set)

headers = {'Authorization': f"Bearer {token_set['token']['accessToken']}"}

get_self_user_data = httpx.get('http://127.0.0.1:8000/api/v1/users/me', headers=headers)

print(get_self_user_data.status_code)
print(get_self_user_data.json())
