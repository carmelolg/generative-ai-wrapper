from services.SentimentalAnalysisService import SentimentalAnalysisService
from services.ClassifierService import ClassifierService

#sentimentalAnalyzer = SentimentalAnalysisService()
#sentiment = sentimentalAnalyzer.run('La mia ragazza mi ha lasciato', 'italiano')
#print(sentiment)

classifier = ClassifierService()
_class = classifier.run("Sono alto 184 cm e mi piace molto andare allo stadio. Cosa sono?", ['Uomo', 'Donna', 'bambino', 'bambina'])
print(_class)