from services.PoeService import PoeService
from domain.PromptBuilder import PromptBuilder


poeService = PoeService()

promptBuilder = PromptBuilder()
promptBuilder.defineLanguage('italiano')
promptBuilder.definePattern('\n[Domanda]: la mia domanda\n[Risposta]: la tua risposta\n')
promptBuilder.defineAdditionalContext('Usa come prima fonte il menu che ti ho passato in input')
promptBuilder.defineQuestion("Di cosa parla il file in input?")

poeService.chat(promptBuilder.build(), ['https://irp.cdn-website.com/2cc0bde3/files/uploaded/menu%20completo%20pdf.pdf'])
