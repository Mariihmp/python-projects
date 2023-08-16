import tkinter as tk
import time





def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, update_time)  # Update every 1000ms (1 second)

app = tk.Tk()
app.title("Digital Clock App")
app.geometry("500x250")

label = tk.Label(app, text="", font=("Helvetica", 30), bg="white", relief="solid", borderwidth=3, padx=5, pady=2.5,
                 bd=10)
label.pack(fill="both", expand=True)

update_time()  # Initial call to start updating time

app.mainloop()