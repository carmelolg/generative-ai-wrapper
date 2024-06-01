from services.llm.LLMBuilder import LLMBuilder
from domain.PromptBuilder import PromptBuilder


class SentimentalAnalysisService(object):

    def run(self, message: str, lang='English') -> str:
        llm_service = LLMBuilder().build()

        prompt_builder = PromptBuilder()
        prompt_builder.language(lang)
        # prompt_builder.definePattern('\n[Sentiment] La tua risposta\n')
        prompt_builder.additional_requirements(
            'Your response will be used by a Python library to enable software utilizing AI.')
        prompt_builder.additional_requirements(
            'What will be provided as input to you is a sentence to be categorized based on sentiment.')
        prompt_builder.question(message)

        return llm_service.chat(prompt_builder.build())
