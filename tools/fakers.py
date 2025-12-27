import time


def generate_random_email() -> str:
    return f'test.{time.time()}@example.com'