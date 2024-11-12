import pdfplumber
import voices


def get_first_page() -> str:
    page_text = ""
    with pdfplumber.open("pdf_file.pdf") as pdf:
        first_page = pdf.pages[0]
        pdf_data = first_page.chars

        for data in pdf_data:
            page_text += data["text"]
    return page_text


def tts_api(text: str, filename: str):
    gen_voice = voices.GenerateVoices()
    gen_voice.generate_cloudtts(text, filename)


p2text = get_first_page()
print(p2text)
tts_api(p2text, "pdfaudio.mp3")
