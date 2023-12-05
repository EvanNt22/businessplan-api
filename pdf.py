from pypdf import PdfReader

def main(path=None):
    if path == None:
        path = input("Please enter the path for the pdf: \n")
    reader = PdfReader(path)
    number_of_pages = len(reader.pages)
    text = []
    for n in range(number_of_pages):
        page = reader.pages[n]
        text += [page.extract_text()]

    t = "\n".join(text)
    return t

