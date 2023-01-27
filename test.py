import os
from gtts import gTTS

text = "This is the allways. This is the second sentence. This is the third sentence."


def read_text(text):
    tts = gTTS(text=text, lang='en')
    tts.save("audio.mp3")
    os.system("mpg3 audio.mp3")


read_text(text)
