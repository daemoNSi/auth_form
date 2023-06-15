from tree_data import show_tree
from tkinter import *
from tkinter import ttk
from backend import *
from tkinter import messagebox
from test import *

def raise_frame(frame):
    frame.tkraise()


window = Tk()
window.title('AuthForm')
window.geometry('1350x350')

login_page = Frame(window)
register_page = Frame(window)
operating_window_user = Frame(window)
operating_window_admin = Frame(window)

menubar = Menu(window)
window.config(menu=menubar)
filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label='sth')
filemenu.add_command(label='sth else')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.quit)
menubar.add_cascade(label='File', menu=filemenu)

for frame in (login_page, register_page, operating_window_user, operating_window_admin):
    frame.grid(row=0, column=0, sticky='news')

login_status = True


def login():
    global acc, acc_t, u_name, login_status
    check = login_check(entry_user.get(), entry_pass.get())
    validate_var = ValidateLoginData(entry_user.get())
    acc, acc_t, u_name = validate_var.validate()
    store_data_validate(acc, acc_t, u_name)
    if check[0] == True and login_status == True:
        login_status = False
        messagebox.showinfo('Success!',
                            f"Logged in successfully")
        current_time = datetime.now()
        last_login_time = datetime.strftime(current_time, '%y-%m-%d %H:%M:%S')
        mycursor.execute(f'update User_data set last_login="{last_login_time}" where username="{entry_user.get()}"')
        db.commit()
        entry_user.delete(0,END)
        entry_pass.delete(0,END)
        if check[1] == 'user':
            raise_frame(operating_window_user)
        elif check[1] == 'admin':
            raise_frame(operating_window_admin)
        login_status = True
    elif check[0] != True and login_status == True:
        messagebox.showerror('Submission error',
                             f"Incorrect username or password")
    elif not login_status:
        messagebox.showerror('Submission error',
                             'How did you press it again?!')


def clear_frame(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()


switch_button = ttk.Button(login_page,
                       text='Login',
                       command=login)
switch_button.grid(row=2, column=1, sticky='we')

register = ttk.Button(login_page,text='To Registry', command=lambda: raise_frame(register_page), width=15)
register.grid(row=2, column=0, sticky='we')

lbl_user = ttk.Label(login_page,text='username:')
lbl_user.grid(row=0, column=0)
entry_user = ttk.Entry(login_page)
entry_user.grid(row=0, column=1)

lbl_pass = ttk.Label(login_page,text='password:')
lbl_pass.grid(row=1, column=0)
entry_pass = ttk.Entry(login_page, show='*')
entry_pass.grid(row=1, column=1)

lbl_user2 = ttk.Label(register_page,text='set username:')
lbl_user2.grid(row=0, column=0)
entry_user2 = ttk.Entry(register_page)
entry_user2.grid(row=0, column=1)

lbl_pass2 = ttk.Label(register_page,text='set password:')
lbl_pass2.grid(row=1, column=0)
entry_pass2 = ttk.Entry(register_page, show='*')
entry_pass2.grid(row=1, column=1)

lbl_conf_pass2 = ttk.Label(register_page,text='confirm password:')
lbl_conf_pass2.grid(row=2, column=0)
entry_conf_pass2 = ttk.Entry(register_page, show='*')
entry_conf_pass2.grid(row=2, column=1)

lbl_word2 = ttk.Label(register_page,text='set security word:')
lbl_word2.grid(row=3, column=0)
entry_word2 = ttk.Entry(register_page, show='*')
entry_word2.grid(row=3, column=1)

lbl_email2 = ttk.Label(register_page,text='set email:')
lbl_email2.grid(row=4, column=0)
entry_email2 = ttk.Entry(register_page, show='*')
entry_email2.grid(row=4, column=1)

status = True


def add_data_to():
    global status
    submission = add_data(entry_user2.get(), entry_pass2.get(), entry_conf_pass2.get(), entry_word2.get(), entry_email2.get())
    if submission == True and status == True:
        status = False
        messagebox.showinfo('Success!',
                             f"Login info has been successfully processed")
        raise_frame(login_page)
    elif submission != True and status == True:
        messagebox.showerror('Submission error',
                             f"{submission}")
    elif not status:
        messagebox.showerror('Submission error', 'Only one submission is allowed, your data already has been successfully processed')


register2 = ttk.Button(register_page,text='To login page', command=lambda: raise_frame(login_page), width=15)
register2.grid(row=99, column=0)

switch_button2 = ttk.Button(register_page,
                       text='Register',
                       command=add_data_to)
switch_button2.grid(row=99, column=1, sticky='we')

# ---------------------------------------------------USER

def call_add_to_user_info():
    add_to_user_info()

def pull_up_data():
    search_result = search_diff_data(search_entry.get())
    lbl_print['text'] = f'username - {search_result[0][0]}, creation date - ' \
                        f'{search_result[0][1]}, last_login - {search_result[0][2]}, email - {search_result[0][3]}'


search_btn = ttk.Button(operating_window_user, text='Search', command=pull_up_data)
search_btn.grid(row=0, column=0, sticky='nw')
search_entry = ttk.Entry(operating_window_user)
search_entry.grid(row=0, column=1, sticky='nw')
lbl_print = ttk.Label(operating_window_user, text='')
lbl_print.grid(row=0, column=2, sticky='nw')

enter_data = ttk.Button(operating_window_user,text='Enter data',
                           command=add_to_user_info, width=15)
enter_data.grid(row=98, column=0)

back_to_login = ttk.Button(operating_window_user,text='To login page',
                           command=lambda: raise_frame(login_page), width=15)
back_to_login.grid(row=99, column=0)

# ---------------------------------------------------ADMIN
def create_new_table():
    create_new_table(create_entry.get())

def show_table_func():
    print_table(table_entry.get())

def drop_table_func():
    drop_table(drop_entry.get())

def show_all_tables_func():
    get_all_tables(show_all_tables_entry.get())

def get_data_from_table_func():
    get_data_from_table(get_data_from_table_entry.get())

def change_data_func():
    change_data(change_data_entry.get())

def alter_column_func():
    new_list = []
    for i in add_column_entry.get().split(','):
        new_list.append(i)
    alter_column(new_list[0],new_list[1],new_list[2],new_list[3])

create_Btn = ttk.Button(operating_window_admin,text='Create new table',
                           command=create_new_table, width=15)
create_Btn.grid(row=0, column=0)

default_Value = StringVar()
default_Value.set('testing,column1 varchar(16) NOT NULL,column2 int UNSIGNED NOT NULL,id int UNSIGNED PRIMARY KEY NOT NULL AUTO_INCREMENT')

default_db = StringVar()
default_db.set(f'{current_db()}')

create_entry = ttk.Entry(operating_window_admin, textvariable=default_Value, width=200, foreground='grey')
create_entry.bind('<Button-1>', lambda e: create_entry.delete(0, END))
create_entry.grid(row=0, column=1, sticky='news')

back_to_login = ttk.Button(operating_window_admin,text='To login page',
                           command=lambda: raise_frame(login_page), width=15)
back_to_login.grid(row=99, column=0)

table_entry = ttk.Entry(operating_window_admin, width=200)
table_entry.grid(row=1, column=1, sticky='nw')

drop_table_btn = ttk.Button(operating_window_admin,text='Drop table',
                           command=drop_table_func, width=15)
drop_table_btn.grid(row=2, column=0)

drop_entry = ttk.Entry(operating_window_admin, width=200)
drop_entry.grid(row=2, column=1, sticky='nw')

show_table = ttk.Button(operating_window_admin,text='Show table',
                           command=show_table_func, width=15)
show_table.grid(row=1, column=0)

show_all_tables_entry = ttk.Entry(operating_window_admin, width=200, textvariable=default_db)
show_all_tables_entry.grid(row=3, column=1, sticky='nw')

show_all_tables_btn = ttk.Button(operating_window_admin,text='Show all tables',
                           command=show_all_tables_func, width=15)
show_all_tables_btn.grid(row=3, column=0)

get_data_from_table_entry = ttk.Entry(operating_window_admin, width=200)
get_data_from_table_entry.grid(row=4, column=1, sticky='nw')

get_data_from_table_btn = ttk.Button(operating_window_admin,text='Get all data from:',
                           command=get_data_from_table_func, width=15)
get_data_from_table_btn.grid(row=4, column=0)

change_data_btn = ttk.Button(operating_window_admin,text='Change data',
                           command=change_data_func, width=15)
change_data_btn.grid(row=5, column=0)

default_change_data = StringVar()
default_change_data.set('User_data, username=,changed_name, username=,user2')

change_data_entry = ttk.Entry(operating_window_admin, textvariable=default_change_data, width=200, foreground='grey')
change_data_entry.bind('<Button-1>', lambda e: create_entry.delete(0, END))
change_data_entry.grid(row=5, column=1, sticky='news')

add_column_entry = ttk.Entry(operating_window_admin, width=200)
add_column_entry.grid(row=6, column=1, sticky='nw')

add_column_btn = ttk.Button(operating_window_admin,text='Alter columns:',
                           command=alter_column_func, width=15)
add_column_btn.grid(row=6, column=0)

raise_frame(login_page)

window.mainloop()
