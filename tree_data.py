from tkinter import *
from tkinter import ttk
import re
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password',
    database='logindata'
)

mycursor = db.cursor(buffered=True)

# def check_entry(email_to_check):
#     pattern = re.compile(r'\w+@\w+.com|gov')
#     check = pattern.findall(email_to_check)
#     if len(check) != 0:
#         if email_to_check == check[0]:
#             return True
#     else:
#         return False


def checking_data(acc, Hobby, Fav_game, Fav_day):
    entries = [Hobby, Fav_game, Fav_day]
    column_names = ['Hobby', 'Fav_game', 'Fav_day password']
    for entry in zip(entries, column_names):
        if len(entry[0]) > 16 or len(entry[0]) < 4:
            return False, (f'{entry[1]} must be between 4 to 16 characters')
        elif len(entry[0]) == 0:
            return False, f"{entry[0]} is empty"
    mycursor.execute('INSERT INTO User_info (userID, Hobby, Fav_game, Fav_day) VALUES (%s,%s,%s,%s)',
                     (acc, Hobby, Fav_game, Fav_day))
    db.commit()
    return True


def show_tree(account_id):
    win = Toplevel()
    win.title('User data')
    win.geometry('500x250')

    lbl_hobby = ttk.Label(win, text='Hobby')
    lbl_hobby.grid(row=2, column=0, sticky='nw')
    search_hobby = ttk.Entry(win)
    search_hobby.grid(row=2, column=1, sticky='nw')
    lbl_fav_game = ttk.Label(win, text='Favourite game')
    lbl_fav_game.grid(row=3, column=0, sticky='nw')
    search_fav_game = ttk.Entry(win)
    search_fav_game.grid(row=3, column=1, sticky='nw')
    lbl_fav_day = ttk.Label(win, text='Favourite day')
    lbl_fav_day.grid(row=4, column=0, sticky='nw')
    search_fav_day = ttk.Entry(win)
    search_fav_day.grid(row=4, column=1, sticky='nw')
    submit_btn = ttk.Button(win, text='Submit', command=lambda: checking_data(account_id, search_hobby.get(), search_fav_game.get(), search_fav_day.get()), width=15)
    submit_btn.grid(row=5, column=1, sticky='nw')

    win.mainloop()
