import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password',
    database='logindata'
)

mycursor = db.cursor(buffered=True)
#
# mycursor.execute('CREATE TABLE test (sthID int PRIMARY KEY AUTO_INCREMENT, column2 varchar(32), column3 varchar(32))')
# mycursor.execute('CREATE TABLE plop (sthID int PRIMARY KEY AUTO_INCREMENT, column2 varchar(32), column3 varchar(32))')
# mycursor.execute('CREATE TABLE pep (column2 varchar(32), column3 varchar(32), sthID int PRIMARY KEY AUTO_INCREMENT)')
# mycursor.execute('CREATE TABLE testtable (anotherID int PRIMARY KEY AUTO_INCREMENT, column2222 int, FOREIGN KEY(column2222) REFERENCES test(sthID), column3 varchar(32))')
# mycursor.execute('ALTER TABLE plop CHANGE COLUMN sthID sthID int PRIMARY KEY AUTO_INCREMENT AFTER column2')
# mycursor.execute('INSERT INTO test (sthID, column2, column3) VALUES (%s,%s,%s)', (5,'testrow', 'testrow2'))
# mycursor.execute('INSERT INTO test (column2, column3,sthID) VALUES (%s,%s,%s)', ('testrow22', 'testrow222', 6))
# mycursor.execute(
#     'INSERT INTO Accounts (username, password, security_answer, creation_date, last_login, account_type) VALUES (%s,%s,%s,%s,%s,%s)',
#     (entry_user2, entry_pass2, entry_word2, creation_date, last_login, account_type))
# mycursor.execute('insert into test (column2, column3) VALUES (%s,%s)', ('pepkin','popkin'))
# db.commit()



# mycursor.execute('describe testtable')
# for table in mycursor:
#     print(table)
# print('----------------------------------------')
# mycursor.execute('describe test')
# for table in mycursor:
#     print(table)

# mycursor.execute('INSERT INTO testtable (column2222, column3) VALUES (%s,%s)',(6, 'corresponds id6'))
# db.commit()

# mycursor.execute('select test.column2, test.column3, testtable.column3 from test INNER JOIN testtable ON test.sthID = testtable.column2222')
# for table in mycursor:
#     print(table)
# print('----------------------------------------')
# mycursor.execute('select * from test')
# for table in mycursor:
#     print(table)
