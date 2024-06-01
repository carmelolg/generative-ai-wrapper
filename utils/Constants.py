#!/usr/bin/python3
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

import os


class Constants(object):
    poe_token_b = os.environ.get('POE_TOKEN_B', None)
    poe_token_lat = os.environ.get('POE_TOKEN_LAT', None)
    redis_host = os.environ.get('REDIS_HOST', None)
    redis_port = os.environ.get('REDIS_PORT', None)
    poe_model = os.environ.get('POE_MODEL', None)
    local_model = os.environ.get('LOCAL_MODEL', None)
    service = os.environ.get('ACTIVE_SERVICE', 'local')

    __instance = None

    @staticmethod
    def get_instance():
        if Constants.__instance is None:
            Constants()
        return Constants.__instance

    def __init__(self):
        if Constants.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Constants.__instance = self
