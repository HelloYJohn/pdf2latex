# @Author john-y
# @Description TODO
# @Date 2024/4/21 17:36
# @Version 1.0
import os.path
import re

strs = ['A \n',
        'A R \n',
        'A p \n',
        'A G R A p\n',
        'A G R \n',
        'A G R A p \n',
        'A R A G R \n',
        'H \n',
        'G R A \.\. H \n',
        'G \n',
        'R \n',
        'R ,. \n',
        'p A R A G R A p \n',
        'p \n',
        'p ,. \n',
        'p 1\' .,....,.. :., \n',
        '5 . .\'!i.h \n',
        '{: Reading \n',
        '3 . t1., Reading \n',
        '::\\; \'i".r \n',
        'J \)! \' \n',
        '[0-9] \n',
        '[\\\'-. :0-9,·.• "()!{}_;>-]+\n',]


def fullmatchlist(strs, line):
    for str in strs:
        if re.fullmatch(str, line) != None:
            return True
    return False


def tofel_deal(infilepath, outfilepath):
    tmpfile = os.path.basename(infilepath).split()[0]
    with open(tmpfile + "-tmp1.txt", 'w') as outfile:
        with open(infilepath, 'r') as infile:
            for line in infile:
                matchobj1 = re.match('(.*)TOEFL iBT®.*', line)
                if matchobj1 != None:
                    line = matchobj1.group(1) + '\n'

                matchobj2 = re.match('(.*?)�[^A-Za-z0-9 ]+', line)
                if matchobj2 != None:
                    line = matchobj2.group(1) + '\n'

                if fullmatchlist(strs, line):
                    continue
                outfile.write(line)
    with open(tmpfile + "-tmp1.txt", 'r') as infile:
        with open(tmpfile + "-tmp2.txt", 'w') as outfile:
            content = infile.read()
            content = re.sub('®(.*)\n?(.*)\n®(.*)\n?(.*)\n©(.*)\n?(.*)\n®(.*)\n', r'A.\1\2\nB.\3\4\nC.\5\6\nD.\7\n',
                             content, re.S)
            content = re.sub('@(.*)\n?(.*)\n®(.*)\n?(.*)\n©(.*)\n?(.*)\n®(.*)\n', r'A.\1\2\nB.\3\4\nC.\5\6\nD.\7\n',
                             content, re.S)
            content = re.sub('®(.*)\n?(.*)\n@(.*)\n?(.*)\n©(.*)\n?(.*)\n®(.*)\n', r'A.\1\2\nB.\3\4\nC.\5\6\nD.\7\n',
                             content, re.S)
            # content = re.sub('@(.*)\n®(.*)\n©(.*)\n®(.*)\n', r'A. \1\nB. \2\nC. \3\nD. \4\n', content, re.M)
            outfile.write(content)
    with open(outfilepath, 'w') as outfile:
        with open(tmpfile + "-tmp2.txt", 'r') as infile:
            for line in infile:
                if len(line) > 2 and (line[-3:-1] == '. ' or line[-3:-1] == '? '
                                      or line[-3:-1] == 'A ' or line[-3:-1] == 'B '
                                      or line[-3:-1] == 'C ' or line[-3:-1] == 'D '):
                    outfile.write(line)
                else:
                    outfile.write(line[:-1])
    os.remove(tmpfile + "-tmp1.txt")
    os.remove(tmpfile + "-tmp2.txt")

for i in range(4, 11):
    tofel_deal(f'toefl_{i}.txt', f'toefl_{i}_expect.txt')




