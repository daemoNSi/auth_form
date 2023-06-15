import mysql.connector
import re


db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password',
    database='logindata'
)

mycursor = db.cursor(buffered=True)

def create_new_table(*args):
    strin = 'CREATE TABLE '
    new_str = []
    pattern = re.compile(r"[^,]*")
    result = pattern.findall(args[0].strip(''))
    for p in result:
        if p != '':
            new_str.append(p)
    for i in enumerate(new_str):
        if i[0] == 0:
            strin += i[1] + '('
        elif i[0] == len(new_str)-1:
            strin += i[1] + ')'
        else:
            strin += i[1] + ', '
    try:
        mycursor.execute(strin)
        print(f'table {new_str[0]} has been created')
    except:
        print(f'table {new_str[0]} already exists')

def print_table(table):
    mycursor.execute(f'DESCRIBE {table}')
    for x in mycursor:
        print(x)

def get_data_from_table(table):
    mycursor.execute(f'SELECT * from {table}')
    for data in mycursor:
        print(data)

def drop_table(table):
    mycursor.execute(f'DROP TABLE {table}')
    print(f'{table} has been dropped')

def get_all_tables(database):
    mycursor.execute(f'show tables from {database}')
    for table in mycursor:
        print(table[0])

def current_db():
    mycursor.execute('select database()')
    new_str = ''
    for i in mycursor:
        new_str += i[0]
    return new_str

# changing certain data from certain column. f.e. test.change_data('Accounts, account_type=,admin, username=,test123')
def change_data(*args):
    new_str = []
    pattern = re.compile(r"[^,]*")
    result = pattern.findall(args[0].strip(''))
    for p in result:
        if p != '':
            new_str.append(p)
    mycursor.execute((f'update {new_str[0]} set{new_str[1]}"{new_str[2]}" where{new_str[3]}"{new_str[4]}"'))
    db.commit()

def alter_column(action, table, column, config):
    try:
        if action == 'add':
            mycursor.execute(f"ALTER TABLE {table} ADD COLUMN {column} {config} NOT NULL")
            print(f'{column} column was added')
        elif action == 'delete':
            mycursor.execute(f"ALTER TABLE {table} DROP {column}")
            print(f'{column} column was deleted')
    except:
        print('action cannot be performed')

def foreign_table():
    mycursor.execute('CREATE TABLE User_info (userID int PRIMARY KEY,'
                     ' FOREIGN KEY(userID) REFERENCES User_data (accountID), Hobby'
                     ' varchar(32) NOT NULL, Fav_game varchar(32) NOT NULL,'
                     ' Fav_day varchar(32) NOT NULL)')
    print('table has been created')
# def copy_data():
#     mycursor.execute('insert into User_data (accountID, username, password, security_answer, creation_date, last_login, account_type, email)'
#                      ' select accountID, username, password, security_answer, creation_date, last_login, account_type, email from Accounts')
#     print('data was copied')
def delete_data(table, delete_option):
    if delete_option == 'all':
        mycursor.execute(f'DELETE FROM {table}')
        db.commit()
    else:
        for i in delete_option:
            mycursor.execute(f'DELETE FROM {table} WHERE userID={i} limit 1')
            db.commit()
