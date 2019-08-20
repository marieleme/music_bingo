from PyPDF2 import PdfFileMerger

pdfs = []

name = 'BINGO/bingo_sheet'
for i in range(250):
    text = name + str(i) + '.pdf'
    pdfs.append(text)


merger = PdfFileMerger()

for pdf in pdfs:      
    merger.append(pdf)

merger.write("result.pdf")
merger.close()