from persistence.RedisManager import RedisManager
from domain.PromptBuilder import PromptBuilder, Prompt
from utils.Constants import Constants
from poe_api_wrapper import PoeApi
import json


def normalizeThreadId(thread):
    if thread is not None and len(thread) > 0:
        return int(thread)
    else:
        return None


class PoeService(object):
    __db = RedisManager()
    __constants = Constants()

    def __init__(self):
        return

    def tokens(self):
        poeTokenB = self.__constants.poeTokenB
        poeTokenLat = self.__constants.poeTokenLat
        return json.loads(json.dumps({"b": poeTokenB, "lat": poeTokenLat}))

    def chat(self, prompt: Prompt, files: list=[], model=__constants.poeModel):

        if model is None:
            raise Exception("Model is not defined")

        #prompt = (f"Give me a response in 10 word about the following question: {message} "
        #          "The response should have the following pattern [Question]: My question \n[Response]: Your "
        #          "response \n[ChatCode] The chat code")

        prompt = prompt.getFullPrompt()

        thread = self.__db.getValue('poeId')
        thread = normalizeThreadId(thread)

        client = PoeApi(cookie=self.tokens())

        for chunk in client.send_message(self.__constants.poeModel, prompt, chatId=thread, file_path=files):
            print(chunk["response"], end="", flush=True)
        print("\n")

        self.__db.setValue('poeId', chunk['chatId'])
