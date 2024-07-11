from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
NAVY = "#405D72"
GREY = "#758694"
BEIGE = "#F7E7DC"
VINTAGE = "#FFF8F3"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    


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