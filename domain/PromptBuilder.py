class Prompt(object):
    """
    Represents a prompt that will be used to generate a response from a language model.

    Attributes:
        pattern (str): A pattern to guide the language model's elaboration.
        question (str): The question to be answered by the language model.
        language (str): The language of the prompt.
        additional_requirement (str): Any additional requirements for the response.
        file_content (str): Content of a file to be added to the prompt.
    """

    def __init__(self):
        self.pattern = ''
        self.question = ''
        self.language = ''
        self.additional_requirement = ''
        self.file_content = ''

    def __str__(self):
        return f"Prompt: {self.get_full_prompt()}"

    def get_full_prompt(self):
        return 'Hi,\n' + self.file_content + self.question + self.language + self.pattern + self.additional_requirement


class PromptBuilder(object):
    """
    Provides a fluent API for creating prompts.

    Args:
        prompt (Prompt): An optional Prompt object to customize the prompt.
    """

    def __init__(self, prompt: Prompt = None):
        if prompt is None:
            self._prompt = Prompt()
        else:
            self._prompt = prompt

    def language(self, lang):
        self._prompt.language += f"I'd like ask you to answer in this language: {lang}\n"
        return self

    def pattern(self, pattern):
        self._prompt.pattern += f"When you elaborate the answer, I gently ask you to follow this pattern: {pattern}\n"
        return self

    def additional_requirements(self, additionalRequirements):
        self._prompt.additional_requirement += f"Please, I'd like that your response consider also to {additionalRequirements}\n"
        return self

    def question(self, message):
        self._prompt.question += f"The question is: {message}\n"
        return self

    def file(self, filename, content):
        self._prompt.file_content += f"I'm adding a file with the name {filename}, the content of this file is:\n{content}\n"
        return self

    def build(self):
        return self._prompt
