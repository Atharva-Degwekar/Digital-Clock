import time
import tkinter as tk

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    root.after(1000, update_clock)

root = tk.Tk()
root.title("Digital Clock")
label = tk.Label(root, font=("Helvetica", 48), fg="black", bg="white")
label.pack()

update_clock()
root.mainloop()