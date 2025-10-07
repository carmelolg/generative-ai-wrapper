
from langchain_ollama import ChatOllama
from langchain_community.llms.ollama import OllamaEndpointNotFoundError

from lib.persistence.RedisManager import RedisManager
from lib.domain.PromptBuilder import Prompt, PromptBuilder
from lib.services.llm.AbstractLLM import AbstractLLM
from lib.utils.Constants import Constants

from lib.utils.ImageUtils import ImageUtils
from lib.utils.Logger import Logger


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
