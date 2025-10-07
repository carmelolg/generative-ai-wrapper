import json

from poe_api_wrapper import PoeApi

from lib.domain.PromptBuilder import Prompt
from lib.persistence.RedisManager import RedisManager
from lib.services.llm.AbstractLLM import AbstractLLM
from lib.utils.Constants import Constants


def normalize_thread_id(thread):
    if thread is not None and len(thread) > 0:
        return int(thread)
    else:
        return None


class Poe(AbstractLLM):
    __db = RedisManager()
    __constants = Constants.get_instance()

    def __init__(self):
        return

    def tokens(self):
        poe_token_b = self.__constants.poe_token_b
        poe_token_lat = self.__constants.poe_token_lat

        if poe_token_b is None or poe_token_lat is None:
            raise Exception("Poe token missed. Please set on the environment the tokenB and the tokenLat")

        return json.loads(json.dumps({"p-b": poe_token_b, "p-lat": poe_token_lat}))

    def chat(self, prompt: Prompt, files: list = [], model=__constants.poe_model) -> str:

        if model is None:
            raise Exception("Model is not defined")

        prompt = prompt.get_full_prompt()

        thread = self.__db.get_value('poeId')
        thread = normalize_thread_id(thread)

        client = PoeApi(tokens=self.tokens())

        response = ''

        for chunk in client.send_message(self.__constants.poe_model, prompt, chatId=thread, file_path=files):
            response += chunk['response']
            print(".", end="", flush=True)
        print("\n")

        self.__db.set_value('poeId', chunk['chatId'])

        return response
