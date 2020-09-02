from PyPDF2 import PdfFileMerger
from tqdm import tqdm
import config as cf

pdfs = []

for i in tqdm(range(cf.AMOUNT_SHEETS)):
    text = cf.BINGO_FOLDER + cf.SHEET_NAME + str(i) + cf.PDF
    pdfs.append(text)


merger = PdfFileMerger()

for pdf in tqdm(pdfs):      
    merger.append(pdf)

merger.write(cf.MERGED_BINGO_SHEETS)
merger.close()