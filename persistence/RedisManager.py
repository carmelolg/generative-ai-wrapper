import redis
from utils.Constants import Constants


class RedisManager(object):
    __redis = None
    __constants = Constants

    def __init__(self):
        self.__redis = redis.Redis(host=self.__constants.redis_host, port=self.__constants.redis_port)

    def get_value(self, key):
        return self.__redis.get(key)

    def set_value(self, key, value):
        self.__redis.set(key, value)

    def db(self):
        return self.__redis
