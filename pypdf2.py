import PyPDF2

FILE_PATH =  'C:\\Users\\user\\Downloads\\EMPLOYEE NDA.pdf'

with open(FILE_PATH, mode='rb') as f:

    reader = PyPDF2.PdfFileReader(f)

    page = reader.getPage(0)

    print(page.extractText())
