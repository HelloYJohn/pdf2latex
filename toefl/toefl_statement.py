# @Author john-y
# @Description TODO
# @Date 2024/4/21 10:46
# @Version 1.0
import psycopg2
def toefl_ibt_split_to_statement(filepath):
    with open(filepath) as infile:
        conn_info = "dbname=postgres user=john-y password=password host=127.0.0.1"
        conn = psycopg2.connect(conn_info)
        cur = conn.cursor()
        for line in infile:
            listst = line[:-1].split('.')
            for st in listst:
                trimst = st.strip()
                if (len(trimst) != 0):
                    sql = "insert into toefl.toefl_statement values (%s)"
                    cur.execute(sql, (trimst,))

        conn.commit()
        cur.close()


for i in range(1, 11):
    toefl_ibt_split_to_statement(f'toefl_{i}_expect.txt')
# print("READING\n".split('.'))