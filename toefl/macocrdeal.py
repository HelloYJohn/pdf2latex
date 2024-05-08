# @Author john-y
# @Description TODO
# @Date 2024/4/19 18:52
# @Version 1.0
import re
import csv

ALLISDIGIT = re.compile('\w+')

with open('words.csv', 'w', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    with open('/Users/john-y/Downloads/托福核心词组.txt', 'r') as f:
        flag = True
        for line in f:
            if flag == True:
                print(f'{line[:-1]},', end='')
                flag = False
            else:
                print(line, end='')
                flag = True