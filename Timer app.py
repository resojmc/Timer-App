#WIP, Can only set timer once, then program must be restarted to set again.
import tkinter as tk
import time, datetime

root = tk.Tk()
root.geometry("250x250")
root.title("Timer")


def countdown(hour, mins, secs):
    total_seconds = hour * 3600 + mins * 60 + secs
    timer = datetime.timedelta(seconds = total_seconds)
    time_label.config(text=f"{timer}", font=("Ariel", 30))
    if total_seconds > 0:
        root.after(1000, countdown, hour, mins, secs-1)
    else:
        time_label.config(text="Time's up!", font=("Ariel", 30))
        

def start_timer():
    hour = int(hour_entry.get())
    mins = int(min_entry.get())
    secs = int(sec_entry.get())
    time_label.config(text=f"{hour}:{mins}:{secs}", font=("Ariel", 30))
    countdown(hour, mins, secs)


time_label = tk.Label(root, text=f"0:00:00", font=("Ariel", 30))
time_label.pack()

start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.place(x=177, y=220)

hour_label = tk.Label(root, text="Hours: ", font=("Ariel", 10))
hour_label.place(x=0, y=176)

hour_entry = tk.Entry(root, width=10)
hour_entry.place(x=45, y=178.5)

min_label = tk.Label(root, text="Minutes: ", font=("Ariel", 10))
min_label.place(x=0, y=200)

min_entry = tk.Entry(root, width=10)
min_entry.place(x=56, y=202.5)

sec_label = tk.Label(root, text="Seconds: ", font=("Ariel", 10))
sec_label.place(x=0, y=225)

sec_entry = tk.Entry(root, width=10)
sec_entry.place(x=61.5, y=226.5)

root.mainloop()