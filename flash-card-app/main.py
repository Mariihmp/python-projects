from tkinter import*
import pandas
import random
import time
BackGr = "light blue"
de_words = pandas.read_csv("words - Sheet1.csv")
to_learn = de_words.to_dict(orient='records')
current_card = {}
#to learn is a dictionary consist of key val language and value the translation
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text="Dutch",fill='black')
    canvas.itemconfig(card_word,text=current_card['dutch'],fill='black')
    canvas.itemconfig(card_background,image=card_front_img)
    window.after(3000, func=bacK_of_card)

def bacK_of_card():

    canvas.itemconfig(card_title,text='English',fill='white')
    canvas.itemconfig(card_word,text=current_card['english'],fill='white')
    canvas.itemconfig(card_background,image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    next_card()
window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BackGr)
flip_timer = window.after(3000, func=bacK_of_card)
#putting front card image
canvas = Canvas(width=800,height=526)
card_front_img = PhotoImage(file="card_front.png")
card_back_img = PhotoImage(file="card_back.png")
card_background = canvas.create_image(400,263,image=card_front_img)
card_title = canvas.create_text(400,130,text='',font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))


canvas.config(bg=BackGr, highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

cross_img = PhotoImage(file="wrong.png")
unknown_button = Button(width=80,height=80,highlightthickness=0,borderwidth=0,image=cross_img,command=next_card)
unknown_button.grid(row=1, column=0)

check_img = PhotoImage(file="right.png")
known_btn = Button(width=80,height=80,highlightthickness=0,borderwidth=0,image=check_img,command=is_known)
known_btn.grid(row=1, column=1)

#if the check button is clicked the card should be
#deleted from the file

next_card()

window.mainloop()

















#TODO: first there is a front card image
#TODO: to button that has images