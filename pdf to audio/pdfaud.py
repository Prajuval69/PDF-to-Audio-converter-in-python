import PyPDF2 as read
import pyttsx3 as aud

book = open('story.pdf', 'rb')
pdfreader = read.PdfReader(book)
pages = len(pdfreader.pages)  # Get the total number of pages

print(pages)

speaker = aud.init()
for i in range(pages):
    page = pdfreader.pages[i]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()


    