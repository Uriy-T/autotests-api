from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.exercises.exercises_client import get_exercises_client, ExerciseCreateRequest
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import generate_random_email

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestDict(
    email=generate_random_email(),
    password='test_password',
    lastName='string',
    firstName='string',
    middleName='string'
)

create_user_response = public_users_client.create_user(create_user_request)

authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)

files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)

create_file_request = CreateFileRequestDict(
    filename='image.png',
    directory='courses',
    upload_file='testdata/image/image.jpg'
)

create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

create_course_request = CreateCourseRequestDict(
    title='Python API testing',
    maxScore=100,
    minScore=10,
    description='Study how to test API with Python',
    estimatedTime='2 weeks',
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)

create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)


create_exercise_client = get_exercises_client(authentication_user)

create_exercise_request = ExerciseCreateRequest(
    title="Exercise 1",
    courseId=create_course_response['course']['id'],
    maxScore=5,
    minScore=1,
    orderIndex=0,
    description="Exercise 1",
    estimatedTime="5 minutes"
)

create_exercise_response = create_exercise_client.create_exercise(create_exercise_request)
print('Create exercise data:', create_exercise_response)
