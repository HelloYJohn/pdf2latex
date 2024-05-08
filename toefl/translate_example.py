# @Author john-y
# @Description TODO
# @Date 2024/4/23 22:42
# @Version 1.0
import csv

from translate.google_translate import translate_proxy


def translate_example(infilepath, outfilepath):
    with open(outfilepath, 'w') as outfile:
        writer = csv.writer(outfile)
        with open(infilepath) as infile:
            reader = csv.reader(infile, delimiter=',')
            for row in reader:
                if (len(row[3]) != 0):
                    tl = translate_proxy(row[3], 'zh-CN', 'en')
                    writer.writerow((row[0], row[1], row[2], row[3], tl))
                else:
                    writer.writerow((row[0], row[1], row[2], None, None))



translate_example('./list_ipa_example_2.csv', 'list_ipa_example_tl_2.csv')