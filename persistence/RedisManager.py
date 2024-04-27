import redis
from utils.Constants import Constants


class RedisManager(object):
    __redis = None
    __constants = Constants

    def __init__(self):
        self.__redis = redis.Redis(host=self.__constants.redisHost, port=self.__constants.redisPort)

    def getValue(self, key):
        return self.__redis.get(key)

    def setValue(self, key, value):
        self.__redis.set(key, value)

    def db(self):
        return self.__redis
