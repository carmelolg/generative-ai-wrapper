from services.PoeService import PoeService
from domain.PromptBuilder import PromptBuilder


class ClassifierService(object):

    def run(self, message: str, categories=(), lang='English') -> str:
        poeService = PoeService()

        promptBuilder = PromptBuilder()
        promptBuilder.defineLanguage(lang)
        promptBuilder.definePattern(f'Use the following categories: {categories}')
        promptBuilder.defineAdditionalContext(
            'Your response will be used by a Python library to enable software utilizing AI.')
        promptBuilder.defineAdditionalContext(
            'What will be provided as input to you is a sentence to be categorized based on the category in input')
        promptBuilder.defineQuestion(message)

        return poeService.chat(promptBuilder.build())
