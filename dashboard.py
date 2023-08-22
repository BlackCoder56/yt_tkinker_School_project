from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import time
import ttkthemes
from tkinter import ttk
import pymysql


# Function to display data in the treeview
def display_table():
    query = 'select * from student'
    my_cursor.execute(query)
    fetched_data = my_cursor.fetchall()
    the_table.delete(*the_table.get_children())
    for data in fetched_data:
        data_list = list(data)
        the_table.insert('', END, values=data_list)


# Funtion to search for student data
def search_4_student():
    def search_it():
        query = 'select * from student where id=%s or name=%s or gender=%s or address=%s'
        my_cursor.execute(query, (id_input.get(), name_input.get(), gender_input.get(), address_input.get()))
        the_table.delete(*the_table.get_children())
        fetched_data = my_cursor.fetchall()
        for data in fetched_data:
            the_table.insert('', END, values=data)

    search_student_window = Toplevel()
    search_student_window.title('Search Student')
    search_student_window.grab_set()
    search_student_window.resizable(False, False)
    id_label = Label(search_student_window, text='Id', font=('times new roman', 20, 'bold'), fg='DeepPink')
    id_label.grid(row=0, column=0, pady=10, padx=10)
    id_input = Entry(search_student_window, font=('times new roman', 20))
    id_input.grid(row=0, column=1, pady=10, padx=10, sticky='w')

    name_label = Label(search_student_window, text='Name', font=('times new roman', 20, 'bold'), fg='DeepPink')
    name_label.grid(row=1, column=0, pady=10, padx=10)
    name_input = Entry(search_student_window, font=('times new roman', 20))
    name_input.grid(row=1, column=1, pady=10, padx=10, sticky='w')

    phone_label = Label(search_student_window, text='Phone', font=('times new roman', 20, 'bold'), fg='DeepPink')
    phone_label.grid(row=2, column=0, pady=10, padx=10)
    phone_input = Entry(search_student_window, font=('times new roman', 20))
    phone_input.grid(row=2, column=1, pady=10, padx=10, sticky='w')

    email_label = Label(search_student_window, text='Email', font=('times new roman', 20, 'bold'), fg='DeepPink')
    email_label.grid(row=3, column=0, pady=10, padx=10)
    email_input = Entry(search_student_window, font=('times new roman', 20))
    email_input.grid(row=3, column=1, pady=10, padx=10, sticky='w')

    address_label = Label(search_student_window, text='Addess', font=('times new roman', 20, 'bold'), fg='DeepPink')
    address_label.grid(row=4, column=0, pady=10, padx=10)
    address_input = Entry(search_student_window, font=('times new roman', 20))
    address_input.grid(row=4, column=1, pady=10, padx=10, sticky='w')

    gender_label = Label(search_student_window, text='Gender', font=('times new roman', 20, 'bold'), fg='DeepPink')
    gender_label.grid(row=5, column=0, pady=10, padx=10)
    gender_input = Entry(search_student_window, font=('times new roman', 20))
    gender_input.grid(row=5, column=1, pady=10, padx=10, sticky='w')

    dob_label = Label(search_student_window, text='DOB', font=('times new roman', 20, 'bold'), fg='DeepPink')
    dob_label.grid(row=6, column=0, pady=10, padx=10)
    dob_input = Entry(search_student_window, font=('times new roman', 20))
    dob_input.grid(row=6, column=1, pady=10, padx=10, sticky='w')

    a_submit_btn = ttk.Button(search_student_window, text='Search', command=search_it)
    a_submit_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=20)


# function for deleting data
def delete_student():
    treeview_index = the_table.focus()
    content = the_table.item(treeview_index)
    content_id = content['values'][0]
    content_name = content['values'][1]
    query = f'delete from student where id = {content_id}'
    my_cursor.execute(query)
    conn.commit()
    display_table()
    messagebox.showinfo('Deleted', f"{content_name}'s data has been deleted successfully!")


# function to add data to student table
def add_student():
    def insert_into_tbl():
        current_date = time.strftime('%d/%m/%Y')
        current_time = time.strftime('%H:%M:%S')
        query = 'insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        my_cursor.execute(query, (id_input.get(), name_input.get(), phone_input.get(), email_input.get()
                                  , address_input.get(), gender_input.get(), dob_input.get(), current_date,
                                  current_time))
        conn.commit()
        display_table()
        response = messagebox.askyesno('Confirm', 'Data added successfully. Do you want to clean the form?',
                                       parent=add_student_window)

        if response:
            id_input.delete(0, END)
            name_input.delete(0, END)
            phone_input.delete(0, END)
            email_input.delete(0, END)
            address_input.delete(0, END)
            gender_input.delete(0, END)
            dob_input.delete(0, END)
        else:
            add_student_window.destroy()

    add_student_window = Toplevel()
    add_student_window.title('Add Student')
    add_student_window.grab_set()
    add_student_window.resizable(False, False)
    id_label = Label(add_student_window, text='Id', font=('times new roman', 20, 'bold'), fg='DeepPink')
    id_label.grid(row=0, column=0, pady=10, padx=10)
    id_input = Entry(add_student_window, font=('times new roman', 20))
    id_input.grid(row=0, column=1, pady=10, padx=10, sticky='W')

    name_label = Label(add_student_window, text='Name', font=('times new roman', 20, 'bold'), fg='DeepPink')
    name_label.grid(row=1, column=0, pady=10, padx=10)
    name_input = Entry(add_student_window, font=('times new roman', 20))
    name_input.grid(row=1, column=1, pady=10, padx=10, sticky='w')

    phone_label = Label(add_student_window, text='Phone', font=('times new roman', 20, 'bold'), fg='DeepPink')
    phone_label.grid(row=2, column=0, pady=10, padx=10)
    phone_input = Entry(add_student_window, font=('times new roman', 20))
    phone_input.grid(row=2, column=1, pady=10, padx=10, sticky='w')

    email_label = Label(add_student_window, text='Email', font=('times new roman', 20, 'bold'), fg='DeepPink')
    email_label.grid(row=3, column=0, pady=10, padx=10)
    email_input = Entry(add_student_window, font=('times new roman', 20))
    email_input.grid(row=3, column=1, pady=10, padx=10, sticky='w')

    address_label = Label(add_student_window, text='Address', font=('times new roman', 20, 'bold'), fg='DeepPink')
    address_label.grid(row=4, column=0, pady=10, padx=10)
    address_input = Entry(add_student_window, font=('times new roman', 20))
    address_input.grid(row=4, column=1, pady=10, padx=10, sticky='w')

    gender_label = Label(add_student_window, text='Gender', font=('times new roman', 20, 'bold'), fg='DeepPink')
    gender_label.grid(row=5, column=0, pady=10, padx=10)
    gender_input = Entry(add_student_window, font=('times new roman', 20))
    gender_input.grid(row=5, column=1, pady=10, padx=10, sticky='w')

    dob_label = Label(add_student_window, text='DOB', font=('times new roman', 20, 'bold'), fg='DeepPink')
    dob_label.grid(row=6, column=0, pady=10, padx=10)
    dob_input = Entry(add_student_window, font=('times new roman', 20))
    dob_input.grid(row=6, column=1, pady=10, padx=10, sticky='w')

    a_submit_btn = ttk.Button(add_student_window, text='Submit', command=insert_into_tbl)
    a_submit_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=20)


# function to connect to the database
def database_connection_function():
    def connect_2_db():

        global my_cursor, conn
        #  if hostname_entry.get() == '' or username_entry.get() == '' or server_password_entry == '':
        #   messagebox.showerror('Error', 'All fields required to connect to the server', parent=popup1)
        # else:
        try:
            conn = pymysql.connect(host='localhost', user='root',
                                   password='swap2')
            my_cursor = conn.cursor()
            # messagebox.showinfo('Success', 'Connection Successful', parent=popup1)

            popup1.destroy()
        except:
            messagebox.showerror('Error', 'Invalid or incorrect details', parent=popup1)

        try:
            query = 'create database student_db'
            my_cursor.execute(query)
            query1 = 'use student_db'
            my_cursor.execute(query1)
            query2 = 'create table student(id int not null primary key, name varchar(30), mobile varchar(10), ' \
                     'email varchar(30), address varchar(40), gender varchar(30),' \
                     'dob varchar(20), date varchar(50), time varchar(50))'
            my_cursor.execute(query2)
        except:
            query3 = 'use student_db'
            my_cursor.execute(query3)
            add_student_btn.config(state=NORMAL)
            search_student_btn.config(state=NORMAL)
            delete_student_btn.config(state=NORMAL)
            update_student_btn.config(state=NORMAL)
            show_student_btn.config(state=NORMAL)
            export_data_btn.config(state=NORMAL)
            display_table()

    popup1 = Toplevel()
    popup1.grab_set()
    popup1.resizable(False, False)
    popup1.title('Connect to the Database')
    popup1.geometry('400x250+840+100')

    hostname = Label(popup1, text='Host name', font=('arial', 14, 'bold'), fg='black')
    hostname.grid(row=0, column=0, padx=20, pady=12)
    hostname_entry = Entry(popup1, font=('arial', 14, 'bold'), fg='black', bd=2)
    hostname_entry.grid(row=0, column=1, padx=10, pady=20)

    username = Label(popup1, text='Username', font=('arial', 14, 'bold'), fg='black')
    username.grid(row=1, column=0, padx=20, pady=12)
    username_entry = Entry(popup1, font=('arial', 14, 'bold'), fg='black', bd=2)
    username_entry.grid(row=1, column=1, padx=10, pady=12)

    server_password = Label(popup1, text='Password', font=('arial', 14, 'bold'), fg='black')
    server_password.grid(row=2, column=0, padx=20, pady=12)
    server_password_entry = Entry(popup1, font=('arial', 14, 'bold'), fg='black', show='*', bd=2)
    server_password_entry.grid(row=2, column=1, padx=10, pady=12)

    hostname_entry.focus()

    con_btn = ttk.Button(popup1, text='Connect', width=30, command=connect_2_db)
    con_btn.grid(row=3, column=0, columnspan=2, pady=20)


# function to grab the current time and date
def date_time():
    date = time.strftime('%d/%m/%Y')
    c_time = time.strftime('%H:%M:%S')
    date_time_label.config(text=f'   Date: {date}\nTime: {c_time}')
    date_time_label.after(1000, date_time)


# global variables
count = 0
ini_text = ''


# Title animation
def text_animation():
    global ini_text, count

    if count == len(the_text):
        count = 0
        ini_text = ''

    ini_text = ini_text + the_text[count]
    title_label.config(text=ini_text)
    count = count + 1
    title_label.after(200, text_animation)


# UI Design for the main window [ registration form ]
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

# Button to connect to the database
connect_database = ttk.Button(root, text='Connect to Database', command=database_connection_function)
connect_database.place(x=1050, y=10)

left_frame = Frame(root, width=300, height=600)
left_frame.place(x=10, y=80)

top_image = ImageTk.PhotoImage(file='students.png')
top_image_label = Label(left_frame, image=top_image)
top_image_label.grid(row=0, column=0, pady=20)

# Action buttons
add_student_btn = ttk.Button(left_frame, text='Add Students', width=25, state=DISABLED, command=add_student)
add_student_btn.grid(row=1, column=0, pady=10, padx=10)

search_student_btn = ttk.Button(left_frame, text='Search Students', width=25, state=DISABLED, command=search_4_student)
search_student_btn.grid(row=2, column=0, pady=10)

delete_student_btn = ttk.Button(left_frame, text='Delete Students', width=25, state=DISABLED, command=delete_student)
delete_student_btn.grid(row=3, column=0, pady=10)

update_student_btn = ttk.Button(left_frame, text='Update Students', width=25, state=DISABLED)
update_student_btn.grid(row=4, column=0, pady=10)

show_student_btn = ttk.Button(left_frame, text='Show Students', width=25, state=DISABLED, command=display_table)
show_student_btn.grid(row=5, column=0, pady=10)

export_data_btn = ttk.Button(left_frame, text='Export Data', width=25, state=DISABLED)
export_data_btn.grid(row=6, column=0, pady=10)

logout_btn = ttk.Button(left_frame, text='Logout', width=25)
logout_btn.grid(row=7, column=0, pady=40)

right_frame = Frame(root)
right_frame.place(x=300, y=80, width=960, height=550)

# code for creating scrollbars on the treeview
scrollBar_x = Scrollbar(right_frame, orient=HORIZONTAL)
scrollBar_y = Scrollbar(right_frame, orient=VERTICAL)

# creating treeview
the_table = ttk.Treeview(right_frame, columns=('Id', 'Name',
                                               'Telephone', 'Email',
                                               'Address', 'Gender',
                                               'D.O.B', 'Added Date', 'Added Time',),
                         xscrollcommand=scrollBar_x.set, yscrollcommand=scrollBar_y.set)
# code for mapping scrollbars to the treeview using config method
scrollBar_x.config(command=the_table.xview)
scrollBar_y.config(command=the_table.yview)

# packing / placing the scrollbars to the frame
scrollBar_x.pack(side=BOTTOM, fill=X)
scrollBar_y.pack(side=RIGHT, fill=Y)

the_table.pack(fill=BOTH, expand=1)

# adding column headers
the_table.heading('Id', text='Id')
the_table.heading('Name', text='Name')
the_table.heading('Telephone', text='Telephone')
the_table.heading('Email', text='Email')
the_table.heading('Address', text='Address')
the_table.heading('Gender', text='Gender')
the_table.heading('D.O.B', text='D.O.B')
the_table.heading('Added Date', text='Added Date')
the_table.heading('Added Time', text='Added Time')

# Styling and reducing column size
the_table.column('Id', width=50, anchor=CENTER)
the_table.column('Name', width=150, anchor=W)
the_table.column('Telephone', width=100, anchor=CENTER)
the_table.column('Email', width=150, anchor=W)
the_table.column('Address', width=130, anchor=W)
the_table.column('Gender', width=60, anchor=CENTER)
the_table.column('D.O.B', width=100, anchor=CENTER)
the_table.column('Added Date', width=90, anchor=CENTER)
the_table.column('Added Time', width=80, anchor=CENTER)

# Additional design to the treeview
style = ttk.Style()
style.configure('Treeview', rowheight=20, font=('arial', 12, 'bold'), background='light gray', foreground='black',
                fieldbackground='slate gray')
style.configure('Treeview.Heading', font=('arial', 12, 'bold'), foreground='navy')

the_table.config(show='headings')

root.mainloop()
