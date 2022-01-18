#  @uthor: Dr.-Ing. Joan MOUBA, joan.mouba@gmail.com

import pyttsx3

with open('book_content.txt', 'r', encoding="utf-8") as book:
    book_content = book.read()
    speaker = pyttsx3.init()
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[1].id)  # change index to change voice
    speaker.setProperty("rate", 150)
    speaker.setProperty("volume", 0.9)  # volume 0-1
    speaker.save_to_file(book_content, filename='myaudiobook.mp3')  # to save the audio
    # speaker.say(book_content)  # speaker reads it loud
    speaker.runAndWait()
