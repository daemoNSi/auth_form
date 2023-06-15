import mysql.connector
from datetime import datetime
from tkinter import *
from tkinter import ttk
from tree_data import show_tree

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password',
    database='logindata'
)

mycursor = db.cursor(buffered=True)
current_user = list()
# mycursor.execute('CREATE DATABASE logindata')
# lit = [2,4]
# for i in lit:
#     mycursor.execute(f'DELETE FROM User_data WHERE accountID={i} limit 1')
#     db.commit()

def add_data(entry_user2, entry_pass2, entry_conf_pass2, entry_word2, entry_email2):
    error_list = [entry_user2, entry_pass2, entry_conf_pass2, entry_word2]
    error_message = ['username', 'password', 'confirmation password', 'security word']
    for entry in zip(error_list, error_message):
        if len(entry[0]) > 16 or len(entry[0]) < 4:
            return (f'{entry[1]} must be between 4 to 16 characters')
        elif len(entry[0]) == 0:
            return(f"{entry[0]} is empty")
    if 4 <= len(entry_user2) <= 16 and 4 <= len(entry_pass2) <= 16 and 4 <= len(entry_conf_pass2) <= 16 and 4 <= len(entry_word2) <= 16:
        if entry_pass2 == entry_conf_pass2:
            current_date = datetime.now()
            creation_date = datetime.strftime(current_date, '%y-%m-%d %H:%M:%S')
            last_login = creation_date
            account_type = 'user'
            # add these to the db on click  entry_user2, entry_pass2, entry_word2, creation_date, last_login, account_type
            mycursor.execute('INSERT INTO User_data (username, password, security_answer, creation_date, last_login, account_type, email) VALUES (%s,%s,%s,%s,%s,%s,%s)',
                             (entry_user2, entry_pass2, entry_word2, creation_date, last_login, account_type, entry_email2))
            db.commit()
            return True
        elif entry_pass2 != entry_conf_pass2:
            return(f"passwords don't match")


def change_data(username):
    mycursor.execute(f'update User_data set account_type = "admin" where username = "{username}"')
    db.commit()



def print_data():
    mycursor.execute('SELECT * FROM User_data')
    for x in mycursor:
        print(x)


def login_check(username, password):
    global current_user
    mycursor.execute('SELECT username, password, account_type FROM User_data')
    for entry in mycursor:
        if username == entry[0] and password == entry[1]:
            return True, entry[2]
        elif username != entry[0] or password == entry[1]:
            pass
    return False, 'None'


def search_diff_data(input_data):
    mycursor.execute(f'SELECT username, creation_date, last_login, email FROM User_data where username = "{input_data}"')
    temp_list = []
    for x in mycursor:
        temp_list.append(x)
    return temp_list

acc, acc_t, u_name = '','',''
def add_to_user_info():
    checker = table_info_data()
    hob, gam, day = '','',''
    mycursor.execute(f'select Hobby, Fav_game, Fav_day from USer_info where userID = "{acc}"')
    for i in mycursor:
        hob, gam, day = i
    if checker == True:
        another_lay(hob, gam, day, 'Your data has already been processed')
    elif checker == False:
        show_tree(acc)


def table_info_data():
    mycursor.execute(f'select userID from user_info where userID ="{acc}"')
    row_count = mycursor.rowcount
    if row_count == 0:
        return False
    elif row_count > 0:
        return True


def another_lay(hobby=None, game=None,day=None,lbltext=None):
    another_layer = Toplevel()
    another_layer.title('Data')
    another_layer.geometry('850x250')
    tree = ttk.Treeview(another_layer, columns=('Hobby', 'Favourite game', 'Favourite day'), show='headings',
                        height=5)
    tree.column('#1', anchor=CENTER)
    tree.heading('#1', text='Hobby')
    tree.column('#2', anchor=CENTER)
    tree.heading('#2', text='Favourite game')
    tree.column('#3', anchor=CENTER)
    tree.heading('#3', text='Favourite day')
    mycursor.execute('select Hobby, Fav_Game, Fav_day from user_info')
    tree.pack()
    tree.insert('', 'end', text='1', values=(hobby, game, day))
    lbl_peps = ttk.Label(another_layer, text=lbltext)
    lbl_peps.pack()


def store_data_validate(u,a,a_t):
    global acc, acc_t, u_name
    acc, acc_t, u_name = u,a,a_t


class ValidateLoginData:
    def __init__(self, username):
        self.username = username
        self.acc = ''
        self.acc_t = ''
        self.u_name = ''

    def validate(self):
        mycursor.execute(f'SELECT accountID, account_type, username FROM User_data WHERE username = "{self.username}"')
        for i in mycursor:
            self.acc, self.acc_t, self.u_name = i
        return self.acc, self.acc_t, self.u_name