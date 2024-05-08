# @Author john-y
# @Description TODO
# @Date 2024/4/29 22:29
# @Version 1.0
import re

import PyPDF2


def extract_text_from_pdf(infilepath:str, outfilepath : str, debug = False) -> list:
    pdfFileObj = open(infilepath, 'rb')
    pdfreader = PyPDF2.PdfReader(pdfFileObj)
    if debug:
        print(f";total pages: {len(pdfreader.pages)}")
    with open(outfilepath, 'w') as outfile:
        for page in pdfreader.pages:
            text = page.extract_text()
            outfile.write(text)

def split_text_into_paragraphs(infilepath : str, outfilepath):
    with open(infilepath, 'r') as infile:
        content = infile.read()
        paragraphs = re.split("TPO[\d ]+\n", content)
        # print(len(paragraphs))
        # print(paragraphs[1])
        # # print(paragraphs)
        with open(outfilepath, 'w') as outfile:
            for i in range(1, len(paragraphs)):
                outfile.write("TPO" + str(i) + "\n")
                lines = paragraphs[i].split("\n")
                for line in lines:
                    if (len(line) != 0):
                        if line[-1] == '.' or line[-1] == '?':
                            outfile.write(line + "\n")
                        else:
                            outfile.write(line + " ")


# extract_text_from_pdf('/Users/john-y/Downloads/1-54全部文本/TPO1-54综合口语文本.pdf', './top_spoken1-55.txt')
split_text_into_paragraphs('./top_spoken1-55.txt', './top_spoken_nonl_1-55.txt')