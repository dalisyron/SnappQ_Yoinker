from settings import TEXTPROCESS_DIR
from os.path import join
from hazm import Normalizer

FARSI_DIGITS = '۱۲۳۴۵۶۷۸۹۰'
ENGLISH_DIGITS = '1234567890'
FARSI_ALPHABET = "ئ ا ب پ ت ث ج چ ح خ د ذ ر ز ژ س ش ص ض ط ظ ع غ ف ق ک گ ل م ن و ه ی آ"
ENGLISH_ALPHABET = "A a B b C c D d E e F f G g H h I i J j K k L l M m N n O o P p Q q R r S s T t U u V v W w X x Y y Z z"

def clean(sentence):
    #trim digits
    ind  = 0
    for i in range(len(sentence)):
        if (sentence[i] in FARSI_DIGITS or sentence[i] in ENGLISH_DIGITS):
            ind += 1
        else:
            break
    sentence = sentence[ind:]

    #remove Non-Alphanumeric
    res = []
    for i in range(len(sentence)):
        if (sentence[i] in FARSI_ALPHABET or sentence[i] in FARSI_DIGITS):
            res.append(sentence[i])
    sentence = "".join(res)
    normalizer = Normalizer()
    sentence = normalizer.normalize(sentence)

    return sentence

def mergeLines(line0_str, line1_str):
    if (len(line0_str) == 0):
        return  line1_str
    elif (len(line1_str) == 0):
        return line0_str
    else:
        return line0_str + ' ' + line1_str
