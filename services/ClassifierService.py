from services.llm.LLMBuilder import LLMBuilder
from domain.PromptBuilder import PromptBuilder


class ClassifierService(object):

    def run(self, message: str, categories=(), lang='English') -> str:
        llm_service = LLMBuilder().build()

        prompt_builder = PromptBuilder()
        prompt_builder.language(lang)
        prompt_builder.pattern(f'Use the following categories: {categories}. Don\'t justify the response, just give '
                               f'me only the the category chose.')
        prompt_builder.additional_requirements(
            'what will be provided as input to you is a sentence to be categorized based on the category in input')
        prompt_builder.question(message)

        return llm_service.chat(prompt_builder.build())
