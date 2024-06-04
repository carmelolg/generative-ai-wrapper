

from services.ClassifierService import ClassifierService
from services.SentimentalAnalysisService import SentimentalAnalysisService
from services.SummarizeService import SummarizeService
from services.ChatService import ChatService

#sentimentalAnalyzer = SentimentalAnalysisService()
#sentiment = sentimentalAnalyzer.run('Ho perso 10k€ al casinò questa mattina!', categories=['happiness', 'sadness', 'neutral'], lang='italiano')
#print(sentiment)

classifier = ClassifierService()
_class = classifier.run("I like so much Dragonball", ['Uomo', 'Donna', 'bambino', 'bambina'])
print(_class)

#summarize = SummarizeService()
#_summary = summarize.run('./static/file.txt', 'tell me how much release there is in a year', lang='italiano')
#print(_summary)

#summarize = SummarizeService()
#_summary = summarize.run('./static/article.txt', 'give me why for Carlo Ancellotti was important this match and who are the goal scorers', lang='italiano')
#print(_summary)

#chatService = ChatService()
#_chat = chatService.run(file='./domain/PromptBuilder.py',  message="What the method question do?", lang='english')
#print(_chat)

#chatService = ChatService()
#_chat = chatService.run("Calcolami la derivata della seguente funzione: (1/2)*(cos(x)^2) + (1/ln(x))")
#print(_chat)

#chatService = ChatService()
#_chat = chatService.run(file='./README.md', message="Traducimi in inglese il seguente file")
#print(_chat)