from lib.services.llm.LLMBuilder import LLMBuilder
from lib.domain.PromptBuilder import PromptBuilder


class SentimentalAnalysisService(object):

    def run(self, message: str, categories=(), lang='English') -> str:
        llm_service = LLMBuilder().build()

        prompt_builder = PromptBuilder()
        prompt_builder.language(lang)
        prompt_builder.pattern(f'Use the following categories: {categories}')
        prompt_builder.question(f"Give me the sentiment about this sentence: {message}")

        return llm_service.chat(prompt_builder.build())
