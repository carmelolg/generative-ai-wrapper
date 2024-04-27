
class PromptService(object):
    __prompt = ''

    def defineLanguage(self, lang):
        self.__prompt += f"You must use the following language: {lang}\n"
        pass

    def definePattern(self, pattern):
        self.__prompt += f"You must use the following pattern for the response: {pattern}\n"
        pass

    def defineAdditionalRequirements(self, additionalRequirements):
        self.__prompt += f"Please, pay attention about this requirements: {additionalRequirements}\n"
        pass

    def defineAdditionalContext(self, additionalContext):
        self.__prompt += f"Please, consider this additional context: {additionalContext}\n"
        pass

    def defineMessage(self, message):
        self.__prompt += f"The question is: {message}\n"

    def getPrompt(self):
        return self.__prompt


