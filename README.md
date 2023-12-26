# PDF to Audio Converter

## Description
This Python program uses the PyPDF2 and pyttsx3 libraries to convert text from a PDF file into speech. It extracts text from each page of the PDF and then uses text-to-speech conversion to read the content aloud.

## Features
- **PDF Text Extraction:** Utilizes PyPDF2 to extract text from each page of the provided PDF file.
- **Text-to-Speech Conversion:** Employs pyttsx3 to convert the extracted text into audible speech.
- **Page-by-Page Reading:** Reads the content of each page sequentially.

## Usage
1. Provide the path to the PDF file you want to convert to audio.
2. The program reads each page's text content and converts it into speech.
3. The speech output can be heard as the program progresses through the PDF pages.

## Requirements
- Python 3.x
- PyPDF2 library (for PDF parsing)
- pyttsx3 library (for text-to-speech conversion)

## Instructions
1. Clone the repository or download the Python script.
2. Install the required libraries: `pip install PyPDF2 pyttsx3`
3. Execute the script, providing the path to the PDF file as an argument.

## Example Usage
```bash
python pdf_to_audio.py lp.pdf
