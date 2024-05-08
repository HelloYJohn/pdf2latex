# @Author john-y
# @Description TODO
# @Date 2024/5/8 16:59
# @Version 1.0
import re
from os.path import basename

import psycopg2


def toefl_tpo_insert():
    with open('./top_read_nonl_1-55.txt') as readfile:
        with open('./top_listen_nonl_1-55.txt') as listenfile:
            with open('./top_cw_nonl_1-55.txt') as cwfile:
                with open('./top_spoken_nonl_1-55.txt') as spokenfile:
                    readcontents = re.split("TPO[\d ]+\n", readfile.read())
                    listencontents = re.split("TPO[\d ]+\n", listenfile.read())
                    cwcontents = re.split("TPO[\d ]+\n", cwfile.read())
                    spokencontents = re.split("TPO[\d ]+\n", spokenfile.read())
                    for i in range(1,len(readcontents)):
                        # print('=============================================================================')
                        # print(readcontents[i])
                        # print('=============================================================================')
                        # print(listencontents[i])
                        # print('=============================================================================')
                        # print(cwcontents[i])
                        # print('=============================================================================')
                        # print(spokencontents[i])
                        # break
                        filename = "TPO_" + str(i)
                        reading = readcontents[i]
                        listening = listencontents[i]
                        speaking = spokencontents[i]
                        writing = cwcontents[i]
                        answers = ""
                        conn_info = "dbname=postgres user=john-y password=password host=127.0.0.1"
                        conn = psycopg2.connect(conn_info)
                        cur = conn.cursor()
                        sql = "insert into toefl.tpo_ibt values (%s, %s, %s, %s, %s, %s)"
                        # print((filename, reading, listening, speaking, writing, answers))
                        cur.execute(sql, (filename, reading, listening, speaking, writing, answers))
                        # cur.execute(sql, ['test', 'reading', 'listening', 'speaking', 'writing', 'answers'])

                        # rows = cur.fetchall()
                        # for row in rows:
                        #     print(row)
                        conn.commit()
                        cur.close()
def toefl_tpo_split_line_to_statement(cur, lines):
    for line in lines:
        listst = line[:-1].split('.')
        for st in listst:
            if (st == 'A' or st == 'B' or st == 'C' or st == 'D' or st == 'E' or st == 'F' or st == 'G'
                or st == '1' or st == '2' or st == '3' or st == '4' or st == '5'
                or st == '6' or st == '7' or st == '8' or st == '9' or st == '10' or st == '11' or st == '12' or st == '13' or st == '14'):
                continue
            trimst = st.strip()
            if (len(trimst) != 0):
                sql = "insert into toefl.tpo_statement values (%s)"
                cur.execute(sql, (trimst,))

def toefl_tpo_insert_statement():
    with open('./top_read_nonl_1-55.txt') as readfile:
        with open('./top_listen_nonl_1-55.txt') as listenfile:
            with open('./top_cw_nonl_1-55.txt') as cwfile:
                with open('./top_spoken_nonl_1-55.txt') as spokenfile:
                    readcontents = re.split("TPO[\d ]+\n", readfile.read())
                    listencontents = re.split("TPO[\d ]+\n", listenfile.read())
                    cwcontents = re.split("TPO[\d ]+\n", cwfile.read())
                    spokencontents = re.split("TPO[\d ]+\n", spokenfile.read())
                    for i in range(1,len(readcontents)):
                        # print('=============================================================================')
                        # print(readcontents[i])
                        # print('=============================================================================')
                        # print(listencontents[i])
                        # print('=============================================================================')
                        # print(cwcontents[i])
                        # print('=============================================================================')
                        # print(spokencontents[i])
                        # break
                        reading = readcontents[i]
                        listening = listencontents[i]
                        speaking = spokencontents[i]
                        writing = cwcontents[i]
                        answers = ""
                        conn_info = "dbname=postgres user=john-y password=password host=127.0.0.1"
                        conn = psycopg2.connect(conn_info)
                        cur = conn.cursor()

                        readinglines = reading.split("\n")
                        toefl_tpo_split_line_to_statement(cur, readinglines)
                        listeninglines = listening.split("\n")
                        toefl_tpo_split_line_to_statement(cur, listeninglines)

                        speakinglines = speaking.split("\n")
                        toefl_tpo_split_line_to_statement(cur, speakinglines)

                        writinglines = writing.split("\n")
                        toefl_tpo_split_line_to_statement(cur, writinglines)


                        conn.commit()
                        cur.close()



        conn.commit()
        cur.close()

if __name__ == "__main__":
    # toefl_tpo_insert()
    toefl_tpo_insert_statement()
