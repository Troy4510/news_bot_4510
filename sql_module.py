import sqlite3
import datetime

def check_base(db_name):
    print('[sql.check_base] > ')
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tNews (
    id INTEGER PRIMARY KEY,
    date TEXT,
    time TEXT,
    name TEXT,
    link TEXT,
    public BOOL
    )
    ''')
    connection.commit()
    
    #cursor.execute('INSERT INTO tNews(date,name,link)VALUES ("test_date", "test_name", "test_link")')
    #connection.commit()
    #cursor.execute('DELETE FROM tNews WHERE id > 1') 
    #connection.commit()
    
    connection.close()
    print('[sql.check_base] OK')
    

def add_record(db_name, time, name, link):
    print('[sql.add_record] >')
    in_base = check_record(db_name, link)
    if not in_base:
        print('[sql.add_record] not in base, added')
        date = datetime.datetime.now().strftime('%d.%m.%y')
        query = 'insert into tnews(date,time,name,link) values (?,?,?,?)'
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        cursor.execute(query, (date,time,name,link))
        connection.commit()
        connection.close()
    else:
        print('[sql.add_record] already in base, ignore')


def read_last_records(howmany):
    pass


def read_today_records(db_name):
    print('[sql.read_today_records] >')
    date = datetime.datetime.now().strftime('%d.%m.%y')
    query = f'select * from tnews where (date = "{date}")'
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    connection.close()
    return records
    

def check_record(db_name, link):
    query = f'select * from tnews where (link = "{link}")'
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute(query)
    record = cursor.fetchone()
    connection.close()
    if record == None: 
        return False #нету такой в базе
    else:
        return True

if __name__ == "__main__":
    pass