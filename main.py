from docx2txt import process
import pdfplumber
import gtts
from pathlib import Path
from art import tprint
def text_to_speach(file_path, language, file_name):
    if Path(file_path).is_file():
        print(f'-+- Converting a file {Path(file_path).name} to speech')
        print('-+- Processing...')
        if Path(file_path).suffix == '.txt':
            text = open(file_path, encoding='utf-8').read()
            text.replace('\n', '')
            audio = gtts.gTTS(text, lang=language)
            audio.save(f'{file_name}.mp3')
        if Path(file_path).suffix == '.docx':
            docx = process(file_path)
            docx.replace('\n', '')
            audio = gtts.gTTS(docx, lang=language)
            audio.save(f'{file_name}.mp3')
        if Path(file_path).suffix == '.pdf':
            with pdfplumber.PDF(open(file_path)) as file:
                pages = [page.extract_text() for page in file.pages]
            pdf = ''.join(pages)
            pdf.replace('\n', '')
            audio = gtts.gTTS(pdf, lang=language)
            audio.save(f'{file_name}.mp3')
        return f'-+- Playback of the {Path(file_path).name} in speech was successful!\n--- Have a nice day! ---'
    else:
        return '-+- File not found, check the path to the file and try again!'


tprint('TEXT>>TO>>MP3')
print('-+- Hi! This program allows you to voice your text from files with the extension .txt, .docx, .pdf.')
file_path = input("-+- Enter the path to the file: ")
language = input("-+- Enter the language, for example en, ru: ")
file_name = input("-+- Enter the name of the file in mp3 format: ")
print(text_to_speach(file_path, language, file_name))