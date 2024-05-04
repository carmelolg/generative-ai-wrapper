class Prompt(object):
    def __init__(self):
        self.pattern = ''
        self.question = ''
        self.language = ''
        self.additionalRequirement = ''
        self.additionalContext = ''

    def __str__(self):
        return f"Prompt: {self.getFullPrompt()}"

    def getFullPrompt(self):
        return self.language + self.pattern + self.additionalContext + self.additionalRequirement + self.question


class PromptBuilder(object):

    def __init__(self):
        self.prompt = Prompt()

    def defineLanguage(self, lang):
        self.prompt.language += f"You must use the following language: {lang}\n"
        return self

    def definePattern(self, pattern):
        self.prompt.pattern += f"You must use the following pattern for the response: {pattern}\n"
        return self

    def defineAdditionalRequirements(self, additionalRequirements):
        self.prompt.additionalRequirement += f"Please, pay attention about this requirements: {additionalRequirements}\n"
        return self

    def defineAdditionalContext(self, additionalContext):
        self.prompt.additionalContext += f"Please, consider this additional context: {additionalContext}\n"
        return self

    def defineQuestion(self, message):
        self.prompt.question += f"The question is: {message}\n"
        return self

    def build(self):
        return self.prompt
