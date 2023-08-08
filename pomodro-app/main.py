'''each 20 minutes you take a brak
and repeat this for 4 times
'''
from tkinter import *
import math
import time
#CONSTANTS

#got this from a color pallet "color hunt"
PINK = "#e2979c"
RED = "e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
#TODO:start button , reset button -timer
#25min - 5 min brak *repeat for 4 batch of time
#reset mechansim --------------
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    label.config(text="timer")
    check_marks.config(text="")
    global reps
    reps=0




#start timer
def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN*60
    short_break_sect =SHORT_BREAK_MIN*60
    long_breack_sec = LONG_BREAK_MIN*60
    countdown(work_sec)
    if reps%8==0:
        countdown(long_breack_sec)
        label.config(text="Break",fg=RED)
    elif reps%2 ==0:
        countdown(short_break_sect)
        label.config(text='Break',fg=PINK)
    else:
        countdown(work_sec)
        label.config(text='Work',fg=GREEN)




#countdown mechanism
def countdown(count):
    count_min = math.floor(count/60)
    count_second = count%60
    "245/60 4 min  245%6 seconds "
    if count<10:
        count_second = f"0{count_second}"

    canvas.itemconfig(timer_text, text =f"{count_min}:{count_second}")
    if count>0:
        global timer
        timer = window.after(1000, countdown, count - 1)

    else:
        start_timer()
        mark =''
        work_setion = math.floor(reps/2)
        for _ in range(work_setion):
            mark +='✔'


window = Tk()
window.title("Pomodro Timer")
window.config(padx=100,pady=50,bg=YELLOW)

#label
label = Label()
label.config(font=(FONT_NAME,28,'bold'),fg=GREEN,bg=YELLOW)
label.grid(column=1,row=0)

#canvas
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')#by photo image class
canvas.create_image(100,112,image=tomato_img)
timer_text  = canvas.create_text(100,130,text='00:00',fill='white',font=(FONT_NAME,20,'bold'))
canvas.grid(column=1,row=1)


#button
start_button = Button(text='Start' ,bg=GREEN,borderwidth=0,command=start_timer )
start_button.config(padx=20,pady=10)
start_button.grid(column=0,row=2)

reset_button = Button(text='Reset',bg=GREEN,borderwidth=0,command=reset_timer)
reset_button.config(padx=20,pady=10)
reset_button.grid(column=3,row=2)

#check marks
check_marks = Label(fg='green',bg=YELLOW)
check_marks.grid(column=1,row=3)


window.mainloop()


