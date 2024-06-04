from langchain_community.llms.ollama import OllamaEndpointNotFoundError

from persistence.RedisManager import RedisManager
from domain.PromptBuilder import Prompt, PromptBuilder
from services.llm.AbstractLLM import AbstractLLM
from utils.Constants import Constants

from langchain_community.llms import Ollama

from utils.Logger import Logger


class Langchain(AbstractLLM):
    __db = RedisManager()
    __constants = Constants.get_instance()
    __logger = Logger.get_instance(__name__)

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
                    contents.append((filename, file.read()))

            for content in contents:
                prompt_builder.file(content[0], content[1])

        final_prompt = prompt_builder.build().get_full_prompt()

        self.__logger.info(final_prompt)

        try:
            llm = Ollama(model=model)
            response = llm.invoke(final_prompt)
        except OllamaEndpointNotFoundError:
            raise Exception('Local model not running or not installed')

        return response
