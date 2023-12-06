import os
import secrets

SHORT_LEN = 16
REGULAR = r'^[a-zA-Z0-9]+$'


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URI',
        default='sqlite:///db.sqlite3'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv(
        'SECRET_KEY',
        default=secrets.token_urlsafe(16)
    )
