import tkinter as tk
from time import strftime


root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x100")
root.resizable(False, False)
root.configure(bg='black')
label = tk.Label(root, font=('Arial', 40, 'bold'), bg='black', fg='lime')
label.pack(anchor='center')


def update_time():
    current_time = strftime('%H:%M:%S')
    label.config(text=current_time)
    label.after(1000, update_time)   

update_time()

root.mainloop()