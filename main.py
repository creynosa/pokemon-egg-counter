try:
    from PIL import Image
except ImportError:
    import Image
from PIL import ImageGrab
import pytesseract
from datetime import datetime


def readCounter():
    with open("eggCounter.txt", "r") as f:
        counterVal = int(f.readline())
    return counterVal


def increaseCounter():
    counterVal = readCounter()
    counterVal += 1
    with open("eggCounter.txt", "w") as f:
        f.write(str(counterVal))


if __name__ == "__main__":
    phrases = ["hatched from the e", "hatched fo the", "hatched om the"]

    lastTimeHatched = None
    bbox = (550, 1215, 1800, 1350)
    while True:
        img = ImageGrab.grab(bbox=bbox)
        text = pytesseract.image_to_string(img)
        text = text.strip()

        if any(word in text.lower() for word in phrases):
            currentTime = datetime.now()
            if lastTimeHatched:
                timeElapsed = currentTime - lastTimeHatched
                timeElapsed = timeElapsed.total_seconds()
            else:
                timeElapsed = 10

            if timeElapsed < 10:
                continue

            lastTimeHatched = currentTime
            increaseCounter()
