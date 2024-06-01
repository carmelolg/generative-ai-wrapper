from services.ClassifierService import ClassifierService
from services.SentimentalAnalysisService import SentimentalAnalysisService
from services.SummarizeService import SummarizeService

sentimentalAnalyzer = SentimentalAnalysisService()
sentiment = sentimentalAnalyzer.run('La mia ragazza mi ha lasciato', 'italiano')
print(sentiment)

#classifier = ClassifierService()
#_class = classifier.run("Sono alto 184 cm e mi piace molto andare allo stadio. Cosa sono?", ['Uomo', 'Donna', 'bambino', 'bambina'])
#print(_class)

#summarize = SummarizeService()
#_summary = summarize.run('./static/file.txt', 'tell me how much release there is in a year', lang='italiano')
#print(_summary)
