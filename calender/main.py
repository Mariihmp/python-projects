from tkinter import*
import calendar
from datetime import datetime


year_now = datetime.now().year
text= calendar.calendar(year_now)

window = Tk()
window.geometry('600x650')
window.title("CALANDER")
window.config(background='white')

label_cal = Label(window,text="CALANDER",bg='grey',font=('times',28,'bold'))
label_cal.grid(row=1,column=1)

cal_col = Label(window,text=text,font=('Consolas',10,'bold'))
cal_col.grid(row=2, column=1,padx=20,columnspan=2)

window.mainloop()




