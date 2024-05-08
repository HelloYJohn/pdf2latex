# @Author john-y
# @Description TODO
# @Date 2024/4/20 14:01
# @Version 1.0
import csv

import eng_to_ipa as p
with open('list_ipa.csv', 'w') as outcsvfile:
    writer = csv.writer(outcsvfile, delimiter=',')
    with open('list1.csv', newline='\n') as incsvfile:
        reader = csv.reader(incsvfile, delimiter=',')
        for row in reader:
            writer.writerow((row[0], "[" + p.convert(row[0]) + "]", row[1]))
    # phonetics = p.convert('apple')
    # print(phonetics)