from subprocess import call
from PIL import Image
from settings import IMAGE_DIR
from os.path import join

def saveScreenshot():
  call(["adb","shell","screencap","-p","/sdcard/screen.png"])
  call(["adb","pull","/sdcard/screen.png"])
  call(["adb","shell","rm","/sdcard/screen.png"])

def saveQuestion():
  sc_image = Image.open('screen.png')

  sc_image.crop((32, 280, 683, 352)).save(join(IMAGE_DIR, 'question_line0.png'))
  sc_image.crop((32, 352, 683, 424)).save(join(IMAGE_DIR, 'question_line1.png'))


def saveChoices():
  sc_image = Image.open('screen.png')

  sc_image.crop((90, 479, 642, 550)).save(join(IMAGE_DIR, 'choice0.png'))
  sc_image.crop((90, 572, 642, 643)).save(join(IMAGE_DIR, 'choice1.png'))
  sc_image.crop((90, 665, 642, 736)).save(join(IMAGE_DIR, 'choice2.png'))

def generateImageData():
  saveScreenshot()
  saveQuestion()
  saveChoices()
