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
val = 0
timer=None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_the_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00", font=(FONT_NAME, 16, "bold"))
    tick_label.config(text="")
    timer_label.config(text="timer")




# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global val
    val+=1
    if val==1:
        count_int(5*60)
        timer_label = Label(text="This is the first break", font=(FONT_NAME, 25, "bold"), bg=YELLOW)
        timer_label.grid(column=1, row=1)
    if val==2:
        count_int(5*60)
        tick_label = Label(text="✓", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25, "bold"))
        tick_label.grid(column=1, row=3)
        timer_label = Label(text="This is the second break", font=(FONT_NAME, 25, "bold"), bg=YELLOW)
        timer_label.grid(column=1, row=1)
    if val==3:
        count_int(5*60)
        timer_label = Label(text="This is the third break", font=(FONT_NAME, 25, "bold"), bg=YELLOW)
        timer_label.grid(column=1, row=1)
    if val==4:
        count_int(25*60)
        timer_label = Label(text="This is the fourth break", font=(FONT_NAME, 25, "bold"), bg=YELLOW)
        timer_label.grid(column=1, row=1)
        tick_label = Label(text="✓✓", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25, "bold"))
        tick_label.grid(column=1, row=3)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_int(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec < 10:
        b=str(count_sec)
        sb=b.zfill(2)
        count_sec=sb
    if count_sec==0:
        count_sec="00"



    canvas.itemconfig(timer_text,text=f"{count_min} : {count_sec}",font=(FONT_NAME,16,"bold"))
    if count>0:
        print(count)
        global timer
        timer=window.after(10,count_int,count-1)

    if count==0:
        canvas.itemconfig(timer_text,text="time is up",font=(FONT_NAME,12,"italic"))

    # window.after(1000,count,5)
# ---------------------------- UI SETUP ------------------------------- #


#now making the pomodaro layout

window = Tk()

window.title(" pomodoro technique")
window.configure(bg=YELLOW)
window.configure(padx=200,pady=130)
image1 = PhotoImage(file="tomato.png")

timer_label=Label(text="Timer",font=(FONT_NAME,25,"bold"),bg=YELLOW)
timer_label.grid(column=1,row=1)

canvas = Canvas(bg=YELLOW,highlightthickness=0)
canvas.create_image(200,112,image=image1)
timer_text=canvas.create_text(200,150,text="00:00",font=(FONT_NAME,20,"bold"),fill="white")
canvas.grid(column=1,row=2)

#
start_button=Button(width=5,text="start",fg=RED,command=start_timer)
start_button.grid(columns=1,row=3)

tick_label=Label(text="✓",bg=YELLOW,fg=GREEN,font=(FONT_NAME,25,"bold"))
tick_label.grid(column=1,row=3)

reset_button=Button(width=10,text="reset",fg=RED,command=reset_the_timer)
reset_button.grid(column=3,row=3)



# def functa(a,b,c,d,e):
#     print(f"this is the function that provides a  time delay {a}")
#     print(f"this is the second number {b}")
#     print(f"this is the third number {c}")
#     print(f"this is the fourth number{d}")
#     print(f"this is the fifth number {e}")

# window.after(1000,functa,"hello ","this","is ","shobhit","wayne")



#this is the event driven program

window.mainloop()  #mainloop is the window driven program and this is the continious series