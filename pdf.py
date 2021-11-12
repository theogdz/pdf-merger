
"""
Split PDF
from PyPDF2 import PdfFileWriter, PdfFileReader
input_pdf = PdfFileReader("file1.pdf")
output = PdfFileWriter()
output.addPage(input_pdf.getPage(0))
output.write("first_page.pdf")
"""

"""
Merge PDF
"""
from PyPDF2 import PdfFileReader, PdfFileMerger
from os import listdir
output = PdfFileMerger()
x = listdir(r"C:\Users\guidr\Documents\PDF")
for i in x:
    if i.endswith(".pdf"):
        output.append(PdfFileReader(i))
output.write("merged.pdf")
