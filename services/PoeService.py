from persistence.RedisManager import RedisManager
from utils.Constants import Constants
from poe_api_wrapper import PoeApi
import json


class PoeService(object):
    __db = RedisManager()
    __constants = Constants()

    def __init__(self):
        return

    def tokens(self):
        poeTokenB = self.__constants.poeTokenB
        poeTokenLat = self.__constants.poeTokenLat
        return json.loads(json.dumps({"b": poeTokenB, "lat": poeTokenLat}))

    def chat(self, message, model=__constants.poeModel):

        if model is None:
            raise Exception("Model is not defined")

        prompt = (f"Give me a response in 10 word about the following question: {message} "
                  "The response should have the following pattern [Question]: My question \n[Response]: Your "
                  "response \n[ChatCode] The chat code")

        thread = self.__db.getValue('poeId')

        client = PoeApi(cookie=self.tokens())

        for chunk in client.send_message(self.__constants.poeModel, prompt, chatId=int(thread)):
            print(chunk["response"], end="", flush=True)
        print("\n")

        self.__db.setValue('poeId', chunk['chatId'])

