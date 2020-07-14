import os
import PyPDF2 as p2

wd = os.getcwd()
os.chdir('C:/Users/Donald/Desktop/TestPDF')
print(wd)

PDF = open("bio.pdf", "rb")
pdfread = p2.PdfFileReader(PDF)

#Extracting First Page
x = pdfread.getPage(0)
print(type(x))
for line in x.extractText().splitlines():
    line = line.strip()
    for i in range(100):
        if f"{i}." in line:
            question = line
            while "A." not in line:
                question.append(line)
            print(line)



# print(x.extractText())
# print(pdfread.getIsEncrypted())
# print(pdfread.getDocumentInfo())
# print(pdfread.getNumPages())

#
# Extracting Entire PDF
# i = 0
#
# questions = {}

# while i <pdfread.getNumPages():
#     pageinfo = pdfread.getPage(i)
#
#     print(pageinfo.extractText())
#
#
#     i = i+1



