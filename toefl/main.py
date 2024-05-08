# @Author john-y
# @Description TODO
# @Date 2024/4/8 13:38
# @Version 1.0

import PyPDF2
import re

REWORD1 = re.compile('unknown widths :')
REWORD2 = re.compile('IndirectObject')


def extract_text_from_pdf(filepath:str, debug = False) -> list:
    pdfFileObj = open(
        filepath,
        'rb')
    pdfreader = PyPDF2.PdfReader(pdfFileObj)
    if debug:
        print(f";total pages: {len(pdfreader.pages)}")
    for page in pdfreader.pages[15:65]:
        text = page.extract_text()
        if len(text) != 0:
            for line in text.split('\n'):
                if len(line) != 0:
                    print(f'line: {line}')
                    findres = line.find('unknown widths :')
                    print(f'findres: {findres}')

def extract_text_from_pdf_to_file(infilepath:str, outfilepath, pagei1, pagei2, debug = False) -> list:
    pdfFileObj = open(
        infilepath,
        'rb')
    pdfreader = PyPDF2.PdfReader(pdfFileObj)
    if debug:
        print(f";total pages: {len(pdfreader.pages)}")
    with open(outfilepath, 'w') as outfile:
        for page in pdfreader.pages[pagei1:pagei2]:
            text = page.extract_text()
            outfile.write(text)
# opd pdf
# extract_text_from_pdf('/Users/john-y/Documents/TOEFL/Oxford Picture Dictionary 3rd Edition/Oxford Picture Dictionary 3rd Edition.pdf')
# toefl1pdfpath = '/Users/john-y/Documents/TOEFL/第一册（第4版）真题集+配套音频/托福考试官方真题集1（第4版）.pdf'
# extract_text_from_pdf(toefl1pdfpath, True)
# extract_text_from_pdf_to_file(toefl1pdfpath, 15, 65, './tofel_1.txt', True)
# extract_text_from_pdf_to_file(toefl1pdfpath, './tofel_2.txt', 66, 118, True)
# extract_text_from_pdf_to_file(toefl1pdfpath, './tofel_3.txt', 119, 169, True)
# extract_text_from_pdf_to_file(toefl1pdfpath,  './tofel_4.txt', 172, 221,True)
# extract_text_from_pdf_to_file(toefl1pdfpath,  './tofel_5.txt', 222, 269,True)
toefl2pdfpath = '/Users/john-y/Documents/TOEFL/第二册（第3版）真题集+配套音频/托福考试官方真题集2（第3版）.pdf'
extract_text_from_pdf_to_file(toefl2pdfpath,  './tofel_6.txt', 14, 67,True)
extract_text_from_pdf_to_file(toefl2pdfpath,  './tofel_7.txt', 68, 120,True)
extract_text_from_pdf_to_file(toefl2pdfpath,  './tofel_8.txt', 121, 171,True)
extract_text_from_pdf_to_file(toefl2pdfpath,  './tofel_9.txt', 173, 224,True)
extract_text_from_pdf_to_file(toefl2pdfpath,  './tofel_10.txt', 225, 276,True)