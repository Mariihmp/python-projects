from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)
website = Label(text='Website')

website.grid(row=1, column=0)
website_inp = Entry(width=36)


def add_data():
    website = website_inp.get()
    email = e_inp.get()
    pasword = pass_inp.get()
    if len(website) == 0 or len(pasword) == 0:
        messagebox.showinfo(title='OOps', message='the empty field')
    else:
        is_okay = messagebox.askokcancel(title=website, message=f'These are the details entered  \n email  :{email}'
                                                                f'\n password:  {pasword}\nIs it okay to save?')
        if is_okay:
            with open('data.txt', 'a') as data_file:
                data_file.write(f"{website},{email},{pasword}\n")
            website_inp.delete(0, END)
            e_inp.delete(0, END)
            pass_inp.delete(0, END)




def password_generator():
    all_char = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(11):
        password += random.choice(all_char)

    pass_inp.insert(0, password)
    pyperclip.copy(password)


website_inp.grid(row=1, column=1, columnspan=2)
website_inp.focus()
e_user = Label(text='Email/Username ')

e_user.grid(row=2, column=0)

e_inp = Entry(width=36)
e_inp.grid(row=2, column=1, columnspan=2)

pass_inp = Entry()
pass_inp.grid(row=3, column=1, columnspan=1)

passgen_btn = Button(bg='white', text='Generate Password', command=password_generator)
passgen_btn.grid(row=3, column=2)

password = Label(text='Password ', width=21, height=2, borderwidth=0)
password.grid(row=3, column=0)

add_btn = Button(text='Add', width=34, command=add_data)
add_btn.grid(row=4, column=1, columnspan=2)
add_btn = Button(text='Add', width=32, bg='white', borderwidth=0, command=add_data)

window.mainloop()
