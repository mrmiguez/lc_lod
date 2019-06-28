import requests.exceptions


class LC_LOCException(Exception):
    def __init__(self, message):
        super().__init__(message)


class LCTimeOut(requests.exceptions.ConnectTimeout):
    def __init__(self, message):
        super().__init__(message)


class LinkedDataObjectException(LC_LOCException):
    def __init__(self, message):
        super().__init__(message)
