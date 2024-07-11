from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
NAVY = "#405D72"
GREY = "#758694"
BEIGE = "#F7E7DC"
VINTAGE = "#FFF8F3"
FONT_NAME = "Courier"
WORK_MIN = .1
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


    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Long Break 👏", fg=VINTAGE)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Short Break 👍", fg=GREY)

    else:
        count_down(work_sec)
        label.config(text="Work Time 🫡", fg=NAVY)

    
    count_down()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()
    


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=BEIGE)




label = Label(text="Timer", fg=NAVY, bg=BEIGE, font=("Arial", 45, "bold"))
label.grid(column=1, row=0)


canvas = Canvas(width=200, height=224, bg=BEIGE, highlightthickness=0)
tomato_img = PhotoImage(file="/Users/mo/Desktop/Projects/tkinter-pomodoro-timer/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)





start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset")
reset_button.grid(column=2, row=2)

check_mark = Label(text="✓")
check_mark.grid(column=1, row=4)





window.mainloop()