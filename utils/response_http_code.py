from enum import Enum


class ResponseHttpCode(Enum):
    OK = 200,
    SERVER_GENERAL_ERROR = 500
    NOT_FOUND = 404
    CREATED = 201
