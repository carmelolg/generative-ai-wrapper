from lib.services.ChatService import ChatService

chatService = ChatService()
_chat = chatService.run("Considera il profilo instagram __wvll, ogni foto ha una descrizione che inizia sempre con \"this is what [something] looks like\"."
                        " Un esempio è:\"This is what it looks like when you talk with your friends on the beach."
                        " ."
                        " 📅 2025"
                        " 📍 Fréjus Plage, France"
                        "Puoi generarmi per la foto in input un testo coerente?", file='../static/test.jpg')

print(_chat)
