from services.llm.LLMBuilder import LLMBuilder
from domain.PromptBuilder import PromptBuilder


class SummarizeService(object):

    def run(self, file: str, additional_requirement: str = '', lang='English') -> str:
        llm_service = LLMBuilder().build()

        prompt_builder = PromptBuilder()
        prompt_builder.language(lang)
        prompt_builder.pattern('[Question] My question\n[Response] Your response')
        prompt_builder.additional_requirements(additional_requirement)
        prompt_builder.question(f'Can you summarize this file?')

        return llm_service.chat(prompt_builder.build(), [file])
