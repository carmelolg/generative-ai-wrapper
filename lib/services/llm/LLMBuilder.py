from lib.services.llm.AbstractLLM import AbstractLLM
from lib.services.llm.Langchain import Langchain
from lib.services.llm.Poe import Poe
from lib.utils.Constants import Constants


class LLMBuilder(object):
    __constants = Constants.get_instance()

    def __init__(self, llm: AbstractLLM = __constants.service):
        self._llm = Langchain()
        self.llm(llm)

    def llm(self, llm: AbstractLLM = __constants.service):
        if llm == 'poe':
            self._llm = Poe()
        else:
            # 'local'
            self._llm = Langchain()

    def build(self):
        return self._llm
