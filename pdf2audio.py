import pdfplumber
import argparse
import voices
import sys


def get_n_pages(n: int, file: str) -> str:
    page_text = ""
    with pdfplumber.open(file) as pdf:
        for i in range(n):
            first_page = pdf.pages[i]
            pdf_data = first_page.chars

            for data in pdf_data:
                page_text += data["text"]
    return page_text


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


def main():
    parser = argparse.ArgumentParser(description="PDF 2 Audio generator.")
    parser.add_argument('--pdf', help='The PDF filepath', required=True)
    parser.add_argument("--pages", type=int, help="The number of PDF pages to be converted to audio.", required=True)
    parser.add_argument("--audiofile", help="Audio filepath to be written to.", required=True)

    args = parser.parse_args()

    if args.pdf and args.pages and args.audiofile:
        pdf_file = args.pdf
        no_pages = args.pages
        output_file = args.audiofile
        print(pdf_file, no_pages, output_file)
        p2text = get_n_pages(no_pages, pdf_file)
        print('Generating Audio for\n', p2text)
        tts_api(p2text, output_file)
    else:
        print('Not all aruguments are provided')
        sys.exit()


if __name__ == "__main__":
    main()

