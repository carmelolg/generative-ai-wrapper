from abc import ABC

from lib.domain.PromptBuilder import Prompt


class AbstractLLM(ABC):
    def chat(self, prompt: Prompt, files: list = [], model=''):
        pass
