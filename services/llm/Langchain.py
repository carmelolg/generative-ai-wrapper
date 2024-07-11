import base64

from langchain_community.chat_models import ChatOllama
from langchain_community.llms.ollama import OllamaEndpointNotFoundError
from langchain_core.messages import HumanMessage

from persistence.RedisManager import RedisManager
from domain.PromptBuilder import Prompt, PromptBuilder
from services.llm.AbstractLLM import AbstractLLM
from utils.Constants import Constants

from langchain_community.llms import Ollama

from utils.ImageUtils import ImageUtils
from utils.Logger import Logger


class Langchain(AbstractLLM):
    __db = RedisManager()
    __constants = Constants.get_instance()
    __logger = Logger.get_instance(__name__)
    __image_utils = ImageUtils.get_instance()

    def __init__(self):
        return

    def chat(self, prompt: Prompt, files=[], model=__constants.local_model) -> str:
        prompt_builder = PromptBuilder(prompt)
        if model is None:
            raise Exception("Model is not defined")

        if len(files) > 0:
            contents = []

            for filename in files:
                with open(filename, 'r', errors='ignore') as file:
                    #content = base64.b64encode(file.read()).decode('utf-8')
                    contents.append((filename, file.read()))

            for content in contents:
                prompt_builder.file(content[0], content[1])

        final_prompt = prompt_builder.build().get_full_prompt()

        self.__logger.info(final_prompt)

        try:
            llm = ChatOllama(model=model)
            response = llm.invoke(final_prompt)
        except OllamaEndpointNotFoundError:
            raise Exception('Local model not running or not installed')

        return response.content
