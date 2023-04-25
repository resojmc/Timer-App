#Imports tkinter, time, datetime modules
import tkinter as tk
import time, datetime

#Initiates window and defines its dimensions, title, and its ability to be resized
root = tk.Tk()
root.geometry("250x250")
root.title("Timer")
root.resizable(False, False)


def countdown(hour, mins, secs):
    #Takes total_seconds and displays it as a countdown
    total_seconds = hour * 3600 + mins * 60 + secs
    timer = datetime.timedelta(seconds = total_seconds)
    time_label.config(text=f"{timer}", font=("Ariel", 30))
    if total_seconds > 0:
        time_label.time = root.after(1000, countdown, hour, mins, secs-1)
    else:
        time_label.config(text=f"00:00:00")

def start_stop_timer():
    #Starts timer from given value
    if hasattr(time_label, 'time'):
        root.after_cancel(time_label.time)
    hour = int(hour_entry.get())
    mins = int(min_entry.get())
    secs = int(sec_entry.get())
    countdown(hour, mins, secs)

def reset_button():
    #Stops timer and resets it to 00:00:00
    if hasattr(time_label, 'time'):
        root.after_cancel(time_label.time)
    time_label.config(text=f"00:00:00")
    
time_label = tk.Label(root, text=f"00:00:00", font=("Ariel", 30))
time_label.pack()

reset_button = tk.Button(root, text="Reset", command=reset_button)
reset_button.place(x=205, y=190)

start_button = tk.Button(root, text="Start Timer", command=start_stop_timer)
start_button.place(x=177, y=220)

hour_label = tk.Label(root, text="Hours: ", font=("Ariel", 10))
hour_label.place(x=0, y=176)

hour_entry = tk.Spinbox(root, width=int(2.5), from_=0, to=12, state="readonly")
hour_entry.place(x=45, y=178.5)

min_label = tk.Label(root, text="Minutes: ", font=("Ariel", 10))
min_label.place(x=0, y=200)

min_entry = tk.Spinbox(root, width=int(2.5), from_=0, to=60, state="readonly")
min_entry.place(x=56, y=202.5)

sec_label = tk.Label(root, text="Seconds: ", font=("Ariel", 10))
sec_label.place(x=0, y=225)

sec_entry = tk.Spinbox(root, width=int(2.5), from_=0, to=60, state="readonly")
sec_entry.place(x=61.5, y=226.5)

root.mainloop()