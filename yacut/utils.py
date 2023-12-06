import string
import random

from .models import URLMap


def is_short_id_unique(short_id):
    if URLMap.query.filter_by(short=short_id).first():
        return False
    return True


def get_unique_short_id():
    chars = string.ascii_letters + string.digits
    while True:
        short_id = ''.join(random.choice(chars) for _ in range(6))
        if is_short_id_unique(short_id):
            return short_id
