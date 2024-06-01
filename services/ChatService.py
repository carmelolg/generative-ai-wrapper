from services.llm.LLMBuilder import LLMBuilder
from domain.PromptBuilder import PromptBuilder


class ChatService(object):

    def run(self, message: str, file: str = None, lang='English') -> str:
        llm_service = LLMBuilder().build()

        prompt_builder = PromptBuilder()
        prompt_builder.language(lang)
        prompt_builder.question(message)

        files = []
        if file is not None:
            files.append(file)

        return llm_service.chat(prompt_builder.build(), files)
