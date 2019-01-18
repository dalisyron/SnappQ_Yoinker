import requests
from settings import *
import textprocessor
from datetime import datetime
import spacy
from bs4 import BeautifulSoup

def getResultCount(query, language = None):
    query = query.replace(" ","+")
    query = "https://www.google.com/search?q=" + query
    r = requests.get(query)
    html_doc = r.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    return int(soup.find(id = 'resultStats').text.split()[1].replace(',','')) #About X results

def getMostRelevantAnswer(question, language = None):
    mx = 0
    ind = -1
    cnt = 0
    for i in range(3):
        next_query = question.statement + ' ' + question.choice[i]
        offer = getResultCount(next_query, language)
        print(offer)
        #base_query = question.choice[i]
        #base_offer = getResultCount(base_query, language)
        #if (base_offer != 0):
        #    offer /= base_offer
        if (offer >= mx):
            ind = i
            mx = offer
    print(' ')
    return ind + 1

def getLeastRelevantAnswer(question, language = None):
    mn = 10000000000
    ind = -1
    cnt = 0
    for i in range(3):
        next_query = question.statement + ' ' + question.choice[i]
        offer = getResultCount(next_query, language)
        print(offer)
        # base_query = question.choice[i]
        # base_offer = getResultCount(base_query, language)
        # if (base_offer != 0):
        #    offer /= base_offer
        if (offer <= mn):
            ind = i
            mn = offer
    print(' ')
    return ind + 1

def getAnswer(question, language = None):
    if ('نیست' in question.statement and 'کدام' in question.statement):
        return getLeastRelevantAnswer(question, language)
    else:
        return getMostRelevantAnswer(question, language)

def getSnippets(query, max_ind = 10):
    result = []
    for i in range(1, max_ind, 10):
        url = "https://www.googleapis.com/customsearch/v1?key={}&cx={}&q={}&alt=json&start={}&fields=items(snippet)".format(
            GOOGLE_API_KEY, GOOGLE_UNIVERSAL_ENGINE_KEY, query, i)
        resp = requests.get(url=url)
        data = resp.json()
        try:
            snippets = [snippet_dict['snippet'] for snippet_dict in data['items']]
        except:
            snippets = []
        result = result + snippets
    result = [textprocessor.clean(x) for x in result]
    result = [x for x in result if (len(x) > 5) ]
    return " ".join(result)

def getMostSimilarChoice(question, nlp):
    mx = 0.0
    res = -1

    question_snippets = nlp(getSnippets(question.statement))
    choice_snippets = [nlp(getSnippets(question.choice[i])) for i in range(3)]

    for i in range(3):
        offer = question_snippets.similarity(choice_snippets[i])
        print(question_snippets, choice_snippets[i], offer)
        if (offer > mx):
            mx = offer
            res = i
    return res