from PyPDF2 import PdfFileMerger
import config as cf

pdfs = []

name = 'BINGO/bingo_sheet'
for i in range(cf.AMOUNT_SHEETS):
    text = name + str(i) + '.pdf'
    pdfs.append(text)


merger = PdfFileMerger()

for pdf in pdfs:      
    merger.append(pdf)

merger.write("merged_bingo_sheets.pdf")
merger.close()