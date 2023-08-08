import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        # Create and pack widgets
        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.config(borderwidth=0,fg='purple',font=('Courier',10,'bold'))
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.task_listbox = tk.Listbox(self.root, width=40)
        self.task_listbox.config(borderwidth=0, fg='purple', font=('Courier', 10, 'bold'))
        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)

        self.task_entry.pack(pady=10)
        self.add_button.pack()
        self.task_listbox.pack(pady=10)
        self.delete_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.task_listbox.delete(selected_index)
        else:
            messagebox.showwarning("Warning", "Please select a task to delete!")

if __name__ == "__main__":
    root = tk.Tk()
    root.config(padx=100,pady=50,bg='light blue')
    app = TodoApp(root)
    root.mainloop()
