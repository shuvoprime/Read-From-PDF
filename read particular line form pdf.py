from PyPDF2 import PdfFileReader as readpdf
filename = open("Path_to_the_PDF_File","rb")

pdf=readpdf(filename)
page_no = 2       # I have selected 3rd Page to display its Contents
pagenum = pdf.pages[page_no]   # Since Pages starts counting from '0'

print(pagenum.extractText())

f.close()