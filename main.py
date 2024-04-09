# @Author john-y
# @Description TODO
# @Date 2024/4/8 13:38
# @Version 1.0

import PyPDF2

from google_translate import translate, translate_proxy

pdfFileObj = open('/Users/john-y/Downloads/Transformers-for-Machine-Learning-A-Deep-Dive-by-Taylor-Francis-Group_bibis.ir.pdf', 'rb')
pdfreader = PyPDF2.PdfReader(pdfFileObj)
print(f"pages: {len(pdfreader.pages)}")

for page in pdfreader.pages:
    text = page.extract_text()
    fixtext = text.replace('\n', '')
    # print(fixtext)
    res = translate_proxy(fixtext, "zh-CN", "en")
    print(res)

# res = translate_proxy("Bonjour","zh-CN","en")
# print(res)
