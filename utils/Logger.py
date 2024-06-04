import logging

from utils.Constants import Constants


class Logger(object):
    __constants = Constants.get_instance()

    __instance = None

    __level = logging.INFO
    __format = '%(levelname)s | %(asctime)s | %(name)s | %(message)s'

    if __constants.log_level == 'INFO':
        __level=logging.INFO
    elif __constants.log_level == 'DEBUG':
        __level=logging.DEBUG
    elif __constants.log_level == 'WARNING':
        __level=logging.WARNING
    elif __constants.log_level == 'ERROR':
        __level=logging.ERROR
    else:
        __level=logging.CRITICAL

    logging.basicConfig(format=__format, level=__level)

    @staticmethod
    def get_instance(class_name) -> logging:

        __logger = logging.getLogger(class_name)

        if Logger.__instance is None:
            Logger()

        return __logger

    def __init__(self):
        if Logger.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Logger.__instance = self
