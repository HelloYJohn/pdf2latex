# @Author john-y
# @Description TODO
# @Date 2024/4/19 10:08
# @Version 1.0
import re
import csv

WORD = re.compile('\'[a-zA-Z ().]+\'')
ZHWORD = re.compile('\'[\u4e00-\u9fa5 ;.]+\'')
with open('words.csv', 'w', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    with open('/Users/john-y/Downloads/tofel.md', 'r') as f:
        for line in f:
            en_words = WORD.findall(line)
            zh_words = ZHWORD.findall(line)
            en_words = [word[1:-1].lower() for word in en_words]
            zh_words = [word[1:-1] for word in zh_words]
            if 'List' in en_words:
                en_words.remove('List')
            if '托福核心词组' in zh_words:
                zh_words.remove('托福核心词组')
            zipwords = zip(en_words, zh_words)
            for zipword in zipwords:
                print(zipword)
                csvwriter.writerow(zipword)