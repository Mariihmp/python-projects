# #zerox parc made the first mouse ,
# import tkinter as tk
#
#
# #various types of widgets , buttons ,label, text boxes
#     #adding abel  button text box
#
# window = tk.Tk()
# window.title('my first GUI program')
# window.minsize(width=500,height=400)
# window.config(padx=30,pady =30)
#
#
# label = tk.Label( text='this is a label',font=("Arial",24))
# label.config(text='new Text')
# label.grid(column=0,row=0)
# label.config(padx=40,pady=40)
#
#
# def button_clicked():
#     print("I get clicked ")
#     label .config()
#
# #label
#
#
# #pack place grid
# '''packs every digit at diffrent part , left,right ,center'''
# '''place my_label.place(x=0,y=0) plce it at the specified place'''
#
#
#
# button = tk.Button( text='click me ',command=button_clicked())
# button.grid(column=1,row=2)
#
# button2 = tk.Button(text='new button')
# button2.grid(column=2, row=3)
#
#
# input = tk.Entry(width=18)
# input.get()
# input.grid(column=2,row=2)
# import turtle
#
# tim = turtle.Turtle()
# tim.write("some Text",font=('Times New Roman',80,"bold"))
# #unlimited argument
#
#
#
# tk.mainloop()
'''label , Button , Entry , Text , Spinbox

grid is a tabel version of it label.grid(column=1,
'''

from tkinter import *




window = Tk()
window.title('Miles to kilometer converter')

miles_input = Entry(width=15)
miles_input.grid(column=1,row=0)
miles_label = Label(text='0')
miles_label.grid(column=2,row=0)

def miles_to_kilometer():
    miles = float(miles_input.get())
    km = round(miles*1.609)
    kilometer_result_label.config(text=f"{km}")


is_equal_to = Label(text='is equal to')
is_equal_to.grid(column=0, row=1)

kilometer_result_label = Label(text='0')
kilometer_result_label.grid(column=1,row=1)

kilometer_sign_label = Label(text='KM')
kilometer_sign_label.grid(column=2,row=1)

button = Button(text='calculate',command=miles_to_kilometer)
button.grid(column=2, row=2)

check_box = Checkbutton()
check_box.grid(row=0,column=0)
# check_box.config(width=20,height=20)

window.config(width=80,height=30)
window.config(padx=40,pady=40)


mainloop()
