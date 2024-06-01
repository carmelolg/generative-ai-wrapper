from services.llm.LLMBuilder import LLMBuilder
from domain.PromptBuilder import PromptBuilder


class ChatService(object):

    def run(self, message: str, lang='English') -> str:
        llm_service = LLMBuilder().build()

        prompt_builder = PromptBuilder()
        prompt_builder.language(lang)
        prompt_builder.question(message)

        return llm_service.chat(prompt_builder.build())
