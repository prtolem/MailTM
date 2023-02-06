import random
import string


def random_string(length=8):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


async def validate_response(response) -> bool:
    if response.status in [200, 201, 204]:
        return True
    else:
        return False
