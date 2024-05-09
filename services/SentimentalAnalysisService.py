from services.PoeService import PoeService
from domain.PromptBuilder import PromptBuilder


class SentimentalAnalysisService(object):

    def run(self, message: str, lang='English') -> str:
        poeService = PoeService()

        promptBuilder = PromptBuilder()
        promptBuilder.defineLanguage(lang)
        # promptBuilder.definePattern('\n[Sentiment] La tua risposta\n')
        promptBuilder.defineAdditionalContext(
            'Your response will be used by a Python library to enable software utilizing AI.')
        promptBuilder.defineAdditionalContext(
            'What will be provided as input to you is a sentence to be categorized based on sentiment.')
        promptBuilder.defineQuestion(message)

        return poeService.chat(promptBuilder.build())
