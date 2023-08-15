from tkinter import *
from PIL import ImageTk
import time
import ttkthemes
from tkinter import ttk


def date_time():
    date = time.strftime('%d/%m/%Y')
    c_time = time.strftime('%H:%M:%S')
    date_time_label.config(text=f'   Date: {date}\nTime: {c_time}')
    date_time_label.after(1000, date_time)


count = 0
ini_text = ''


def text_animation():
    global ini_text, count

    if count == len(the_text):
        count = 0
        ini_text = ''

    ini_text = ini_text + the_text[count]
    title_label.config(text=ini_text)
    count = count + 1
    title_label.after(200, text_animation)


root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')
root.resizable(False, False)
root.title("School Management School")
root.iconbitmap('app.ico')
root.geometry('1280x685+-8+0')

bg_image = ImageTk.PhotoImage(file='bg.jpg')
bg_label = Label(root, image=bg_image)
bg_label.place(y=0, x=0)

date_time_label = Label(root, text='Time', font=('Arial', 16, 'bold'), fg='indianRed1')
date_time_label.place(y=10, x=5)
date_time()

the_text = 'Step by Step Secondary School'
title_label = Label(root, text=the_text, font=('Times new roman', 26, 'bold'), fg='DeepPink')
title_label.place(x=400, y=10)
text_animation()

connect_database = ttk.Button(root, text='Connect to Database')
connect_database.place(x=980, y=10)

left_frame = Frame(root, width=300, height=600)
left_frame.place(x=10, y=80)

top_image = ImageTk.PhotoImage(file='students.png')
top_image_label = Label(left_frame, image=top_image)
top_image_label.grid(row=0, column=0, pady=20)

add_student_btn = ttk.Button(left_frame, text='Add Students', width=25)
add_student_btn.grid(row=1, column=0, pady=10, padx=10)

search_student_btn = ttk.Button(left_frame, text='Search Students', width=25)
search_student_btn.grid(row=2, column=0, pady=10)

delete_student_btn = ttk.Button(left_frame, text='Delete Students', width=25)
delete_student_btn.grid(row=3, column=0, pady=10)

update_student_btn = ttk.Button(left_frame, text='Update Students', width=25)
update_student_btn.grid(row=4, column=0, pady=10)

show_student_btn = ttk.Button(left_frame, text='Show Students', width=25)
show_student_btn.grid(row=5, column=0, pady=10)

export_data_btn = ttk.Button(left_frame, text='Export Data', width=25)
export_data_btn.grid(row=6, column=0, pady=10)

logout_btn = ttk.Button(left_frame, text='Logout', width=25)
logout_btn.grid(row=7, column=0, pady=40)

root.mainloop()
