import googletrans

def getEnglishTranslation(sentence):
    translator = googletrans.Translator()
    return translator.translate(sentence, src='fa', dest='en').text