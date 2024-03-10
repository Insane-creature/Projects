from tkinter import *
import math

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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        count_down(work_sec)
        timer.config(text="Work")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Break", fg=PINK)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Break", fg=GREEN)
        
        
        
    count_down(5*60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count -1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer = Label(text="Timer", fg = GREEN, font=(FONT_NAME, 50), bg=YELLOW)
timer.grid(column=1 ,row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness= 0)
tomato_img = PhotoImage(file= "tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100,130,text="00:00", fill= "white" ,font=(FONT_NAME, 30, "bold"))
canvas.grid(column= 1,row=1)

# count_down(5)

start = Button(text="Start", highlightthickness = 0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", bg=YELLOW, highlightthickness= 0)
reset.grid(column= 2,row= 2)

tick = Label(text="✔", fg=GREEN, bg=YELLOW)
tick.grid(column= 1,row= 3)

window.mainloop()