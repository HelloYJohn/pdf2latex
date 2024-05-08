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
            for paragraph in paragraphs:
                lines = paragraph.split("\n")
                for line in lines:
                    if (len(line) != 0):
                        if line.startswith("[ABCDEFG]\."):
                            outfile.write(line + " ")
                        elif line[-1] == '.' or line[-1] == '?':
                            outfile.write(line + "\n")
                        else:
                            outfile.write(line + " ")

def split_text_into_paragraphs_aid(infilepath : str, outfilepath):
    with open(infilepath, 'r') as infile:
        content = infile.read()
        paragraphs = re.split("TPO\d+\n", content)
        with open(outfilepath, 'w') as outfile:
            for i in range(1, len(paragraphs)):
                outfile.write("\n" + "TPO" + str(i))
                lines = paragraphs[i].split("\n")
                for line in lines:
                    if (len(line) != 0):
                        if re.match(r"[ABCDEFG]\..*", line):
                            outfile.write("\n" + line + " ")
                        elif re.match(r"[0-9]+\..*", line):
                            outfile.write("\n" + line + " ")
                        elif re.match(r"[A-Z].*", line):
                            outfile.write("\n" + line + " ")
                        else:
                            outfile.write(line + " ")

# extract_text_from_pdf('/Users/john-y/Downloads/1-54全部文本/新政版TPO1-54阅读左右排版.pdf', './top_read1-55.txt')
# split_text_into_paragraphs('./top_read1-55.txt', './top_read_nonl_1-55.txt')
split_text_into_paragraphs_aid('./top_read1-55.txt', './top_read_nonl_1-55.txt')