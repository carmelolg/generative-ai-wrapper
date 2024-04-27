#!/usr/bin/python3
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

import os


class Constants(object):
    poeTokenB = os.environ.get('POE_TOKEN_B', None)
    poeTokenLat = os.environ.get('POE_TOKEN_LAT', None)
    redisHost = os.environ.get('REDIS_HOST', None)
    redisPort = os.environ.get('REDIS_PORT', None)
    poeModel = os.environ.get('POE_MODEL', None)

    __instance = None

    @staticmethod
    def getInstance():
        if Constants.__instance is None:
            Constants()
        return Constants.__instance

    def __init__(self):
        if Constants.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Constants.__instance = self
