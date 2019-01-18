import screencap
import ocr
import webbrowser
import question
import analyze
from settings import *
import pyautogui
#import spacy
import requests
import pyautogui
import textprocessor

from sys import argv

#nlp = spacy.load(FARSI_MODEL_DATA_DIR)
#print('nlp successfully loaded')
def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

try:
  language = argv[1]
except:
  language = None

try:
  choice = argv[2]
except:
  choice = None

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'



def runGoogle(s):
  webbrowser.get(chrome_path).open('www.google.com/search?q=' + s)

screencap.saveScreenshot()
screencap.saveQuestion()

question_text = textprocessor.clean(ocr.getQuestionText(language))

choice_text = []

if ('کدام' in question_text):
    screencap.saveChoices()
    choice_text = [textprocessor.clean(ocr.getChoiceText(int(choice), language)) for choice in range(3)]


Q = question.Question(statement=question_text, choice_list = choice_text)


def get_url(url):
    response = requests.get(url)

def sendToTelegram(question_no, ans):
    telegram_ids = []
    bot_token = ""

    for ids in telegram_ids:
        base_url = "https://api.telegram.org/{}/sendMessage?chat_id={}&text=Question%20{}%20%20:%20{}".format(bot_token, ids, question_no, ans)
        get_url(base_url)

def altTab():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('tab')

def myOwnThing():
    runGoogle(Q.statement)
    print()
    if ('کدام' in Q.statement):
        for i in range(3):
            runGoogle(Q.choice[i] + ' ' + Q.statement)
        altTab()
        altTab()

if __name__ == '__main__':
    myOwnThing()
    ans = analyze.getAnswer(Q)
    print((str(ans) + ' ') * 1000)
