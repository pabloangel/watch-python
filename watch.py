import tkinter as tk
import time


def update_lcock():
    now = time.strftime("%H:%M:%S")
    label.config(text=now)
    label.after(1000, update_lcock)

app = tk.Tk()
app.title("Watch")
label = tk.Label(app, font=("Helvetica", 300), bg="red", fg="white")
label.pack()

update_lcock()
app.mainloop()

