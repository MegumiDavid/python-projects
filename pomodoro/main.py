
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    global timer_label

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work Time", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(number):
    global timer
    number_min = number//60
    number_seg = number%60

    if len(str(number_min))<2:
        number_min=f'0{number_min}'
    if len(str(number_seg))<2:
        number_seg=f'0{number_seg}'

    canvas.itemconfig(timer_text,text=f"{number_min}:{number_seg}")
    if number > 0:
        timer = window.after(1000,count_down,number - 1)
    else:
        start_timer()



# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(text="Timer",fg=GREEN, bg=YELLOW,font=(FONT_NAME,35,"bold"))
timer_label.grid(column=1,row=0)

canvas = Canvas(window,width=200,height=224)
canvas.config(bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(101,112,image=tomato_img)
timer_text = canvas.create_text(101,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1, row=1)

button_start = Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)

label_checked = Label(text="✓", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME,22,"bold"))
label_checked.config(pady=15)
label_checked.grid(column=1, row=2)

button_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.grid(column=2, row=2)

#count_down()


window.mainloop()