from tkinter import *
from PIL import ImageTk
from tkinter import messagebox


# Login function
def btn_login():
    if username_input.get() == '' or password_input == '':
        messagebox.showerror('Error', 'All fields are required!')
    elif username_input.get() == 'elly' or password_input.get() == '12345':
        messagebox.showinfo('Success', f'Welcome {username_input.get()}\t\t')
        window.destroy()
        import dashboard
    else:
        messagebox.showerror('Error', 'Please enter correct credentials!!')
        username_input.delete(0, END)
        password_input.delete(0, END)
        username_input.focus()


# Login UI Design
window = Tk()
window.iconbitmap('app.ico')
window.title('School management system')
window.geometry('1280x685+-8+0')
window.resizable(False, False)

background = ImageTk.PhotoImage(file='bg.jpg')

bg_label = Label(window, image=background)
bg_label.place(x=0, y=0)

login_frame = Frame(window, bg='white')
login_frame.place(x=420, y=100)

login_image = PhotoImage(file='account.png')

login_image_logo = Label(login_frame, image=login_image, bg='white')
login_image_logo.grid(row=0, column=0, columnspan=3, padx=50, pady=10)

username_image = PhotoImage(file='user.png')
username_label = Label(login_frame, image=username_image, text='Username', font=('times new roman', 18, 'bold'),
                       bg='white', compound=LEFT)
username_label.grid(row=1, column=0, padx=10, pady=10)

username_input = Entry(login_frame, font=('times new roman', 16, 'bold'), bd=2)
username_input.grid(row=1, column=1, padx=10)

password_image = PhotoImage(file='padlock.png')
password_label = Label(login_frame, image=password_image, text='Password', font=('times new roman', 18, 'bold'),
                       bg='white', compound=LEFT)
password_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')

password_input = Entry(login_frame, font=('times new roman', 16, 'bold'), bd=2, width=20, show='*')
password_input.grid(row=2, column=1, padx=10)

login_btn = Button(login_frame, text='Login', font=('arial', 18, 'bold'), fg='white', bg='navy', width=10,
                   activebackground='VioletRed1', activeforeground='white', command=btn_login)
login_btn.grid(row=3, column=0, columnspan=2, pady=30, padx=50)

window.mainloop()
