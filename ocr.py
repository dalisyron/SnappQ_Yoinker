import pytesseract
from PIL import Image
import textprocessor
from settings import IMAGE_DIR
from os.path import join

def getImageLineText(image_name, language = None):
  ocr_str = pytesseract.image_to_string(Image.open(join(IMAGE_DIR, image_name)), lang='fas')
  ocr_str = textprocessor.clean(ocr_str)
  return ocr_str

def getQuestionText(language = None):
  line0_str = getImageLineText('question_line0.png', language)
  line1_str = getImageLineText('question_line1.png', language)

  ocr_str = textprocessor.mergeLines(line0_str, line1_str)

  return ocr_str

def getChoiceText(num, language = None):
  return getImageLineText('choice' + str(num) + '.png', language)