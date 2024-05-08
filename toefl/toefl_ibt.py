from os.path import basename

import psycopg2
def toefl_ibt_split(filepath):
    with open(filepath) as infile:
        file_content = infile.read();
        file_len = len(file_content)
        reading_begin = file_content.find('READING')
        listening_begin = file_content.find('LISTENING')
        writing_begin = file_content.find('WRITING')
        speaking_begin = file_content.find('SPEAKING')
        answers_begin = file_content.find('ANSWERS')
        # print(f'reading_begin: {reading_begin}\n'
        #       f'listening_begin: {listening_begin}\n'
        #       f', writing_begin: {writing_begin}\n'
        #       f'speaking_begin: {speaking_begin}\n'
        #       f'answers_begin: {answers_begin}\n'
        #       f'file_len: {file_len}')
        fileallname = basename(filepath)
        filename = fileallname.split('.')[0]
        reading = file_content[reading_begin:listening_begin]
        listening = file_content[listening_begin:speaking_begin]
        writing = file_content[speaking_begin:writing_begin]
        speaking = file_content[writing_begin:answers_begin]
        answers = file_content[answers_begin:file_len]

        # print(reading)
        # print('=============================================================================')
        # print(listening)
        # print('=============================================================================')
        # print(writing)
        # print('=============================================================================')
        # print(speaking)
        # print('=============================================================================')
        # print(answers)
        conn_info = "dbname=postgres user=john-y password=password host=127.0.0.1"
        conn = psycopg2.connect(conn_info)
        cur = conn.cursor()
        sql = "insert into toefl.toefl_ibt values (%s, %s, %s, %s, %s, %s)"
        # print((filename, reading, listening, speaking, writing, answers))
        cur.execute(sql, (filename, reading, listening, speaking, writing, answers))
        # cur.execute(sql, ['test', 'reading', 'listening', 'speaking', 'writing', 'answers'])

        # rows = cur.fetchall()
        # for row in rows:
        #     print(row)
        conn.commit()
        cur.close()



# @Author john-y
# @Description TODO
# @Date 2024/4/20 23:08
# @Version 1.0
for i in range(1, 11):
    toefl_ibt_split(f'toefl_{i}_expect.txt')