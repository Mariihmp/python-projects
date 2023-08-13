
import tkinter as tk
from PIL import Image,ImageTk
import requests

window = tk.Tk()
window.title('kaneye qoute')
window.config(padx=50,pady=50)


def showing_quote():
    response = requests.get('https://api.kanye.rest')
    api_quote = response.json()['quote']
    canvas.itemconfig(quote_text,text=api_quote)


canvas = tk.Canvas(width=300,height=414)
background = tk.PhotoImage(file='background.png',)
canvas.create_image(150,207,image=background)

quote_text = canvas.create_text(150,207,text='kaneye quote ',width=250,font=('Arial',14,'bold'))
canvas.grid(row=0,column=0)

kanye_img = tk.PhotoImage(file='kanye.png')
kanye_btn = tk.Button(image=kanye_img,highlightthickness=0,command=showing_quote)
kanye_btn.grid(row=1,column=0)





window.mainloop()


#error 404 not found
#2,xxx here you go , 3xx go away , 1xx hold on
#5xx i screwd