import pyPdf

def getPDFContent(path):
    content = ""
    # Load PDF into pyPDF
    pdf = pyPdf.PdfFileReader(file(path, "rb"))
    # Iterate pages
    for i in range(0, pdf.getNumPages()):
        # Extract text from page and add to content
        content += pdf.getPage(i).extractText() + "\n"
    # Collapse whitespace
    content = " ".join(content.replace(u"\xa0", "").strip().split())
    return content


# with open('sample.txt', 'w+') as the_file:
#     the_file.write(getPDFContent("sample.pdf").encode("ascii", "ignore"))

with open('sample2.txt', 'w+') as the_file:
    the_file.write(getPDFContent("pdf-sample.pdf").encode("ascii", "ignore"))
