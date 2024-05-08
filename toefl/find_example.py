# @Author john-y
# @Description TODO
# @Date 2024/4/23 22:02
# @Version 1.0
import csv

# select * from toefl_statement;

import psycopg2
def find_example(infilepath, outfilepath=None):
    with open(outfilepath, 'w') as outfile:
        writer = csv.writer(outfile)
        with open(infilepath) as infile:
            conn_info = "dbname=postgres user=john-y password=password host=127.0.0.1"
            conn = psycopg2.connect(conn_info)
            cur = conn.cursor()
            reader = csv.reader(infile, delimiter=',')
            for row in reader:
                # print(row[0])
                cell = row[0].replace('one\'s', '%')
                cell = cell.replace('...', '%')
                cell = cell.replace('\'', '\\\'')
                cell = cell.replace('do sth.', '')
                # print(cell)
                if cell.startswith('be'):
                    execute_sql_be(cell, cur, row, writer)
                else:
                    execute_sql(cell, cur, row, writer)


            cur.close()


def execute_sql(cell, cur, row, writer):
    sql = f"SELECT * FROM toefl.toefl_statement where statement like e'%{cell}%'"
    # print(sql)
    cur.execute(sql)
    frows = cur.fetchall()
    if len(frows) > 0:
        for frow in frows:
            print(row[0], " : ", frow[0])
            writer.writerow((row[0], row[1], row[2], frow[0]))
            break;
    else:
        sql = f"SELECT * FROM toefl.tpo_statement where statement like e'%{cell}%'"
        # print(sql)
        cur.execute(sql)
        frows = cur.fetchall()
        if len(frows) > 0:
            for frow in frows:
                print(row[0], " : ", frow[0])
                writer.writerow((row[0], row[1], row[2], frow[0]))
                break;
        else:
            writer.writerow((row[0], row[1], row[2], None))

def execute_sql_be(cell, cur, row, writer):
    iscell = cell.replace('be', 'is')
    arecell = cell.replace('be', 'are')
    amcell = cell.replace('be', 'am')
    wascell = cell.replace('be', 'was')
    werecell = cell.replace('be', 'were')
    sql = (f"SELECT * FROM toefl.toefl_statement where statement like e'%{iscell}%' "
           f"or statement like e'%{arecell}%' or statement like e'%{amcell}%' or statement like e'%{wascell}%'"
           f"or statement like e'%{werecell}%'")
    print(sql)
    cur.execute(sql)
    frows = cur.fetchall()
    if len(frows) > 0:
        for frow in frows:
            print(row[0], " : ", frow[0])
            writer.writerow((row[0], row[1], row[2], frow[0]))
            break;
    else:
        sql = (f"SELECT * FROM toefl.toefl_statement where statement like e'%{iscell}%' "
               f"or statement like e'%{arecell}%' or statement like e'%{amcell}%' or statement like e'%{wascell}%'"
               f"or statement like e'%{werecell}%'")
        print(sql)
        cur.execute(sql)
        frows = cur.fetchall()
        if len(frows) > 0:
            for frow in frows:
                print(row[0], " : ", frow[0])
                writer.writerow((row[0], row[1], row[2], frow[0]))
                break;
        else:
            writer.writerow((row[0], row[1], row[2], None))

find_example('../list_ipa.csv', 'list_ipa_example_2.csv')
# repstr = "at one's convenience".replace('\'', '\\\'')
# print("at one's convenience".replace('\'', '\\\''))
# print(repstr)