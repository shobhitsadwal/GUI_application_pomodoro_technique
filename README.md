# GUI_application_pomodoro_technique
## A GUI dektop application made by me to use the Pomodoro technique to save the time and more focus and productivity in the work environment


![mover](https://media-exp1.licdn.com/dms/image/C4E12AQEG9zbXa6R1Yw/article-cover_image-shrink_720_1280/0/1567472591506?e=1648080000&v=beta&t=hBDoD2zL5RzEoT4Hw7jvLQdceVPi4vs5AXyBBWUmjLQ)

## here is the Desktop application that I have made 

![pomo](https://pbs.twimg.com/media/Ey40rT9WUA05P_d?format=jpg&name=900x900)

## what is the use of Pomodoro and why it is so effecient ? 

### The Pomodoro Technique was developed in the late 1980s by then university student Francesco Cirillo. Cirillo was struggling to focus on his studies and complete assignments. Feeling overwhelmed, he asked himself to commit to just 10 minutes of focused study time. Encouraged by the challenge, he found a tomato (pomodoro in Italian) shaped kitchen timer, and the Pomodoro technique was born.
    Get a to-do list and a timer.

    Set your timer for 25 minutes, and focus on a single task until the timer rings.

    When your session ends, mark off one pomodoro and record what you completed.

    Then enjoy a five-minute break.

    After four pomodoros, take a longer, more restorative 15-30 minute break.
    
    
### The rule applies even if you do finish your given task before the timer goes off. Use the rest of your time for overlearning, or improving skills or scope of knowledge. For example, you could spend the extra time reading up on professional journals or researching networking opportunities.


# Aim and objectives 
  make a pomodoro shaped alarm clock that has the functionality of displaying work time or free time .

# Requirements 
  this project requires the knowledge of GUI capable software , we have chosen TKINTER python GUI library that is powerful enough to make small scale desktop applications . 
  we have to have to use the math module to complete the program using some of the mathematical tools.
  
# refrences

```main.py/``` for the whole application programming interface
```tomato.png/``` image used for creating the boiler plate and the theme for the whole User Interface

# steps 
- creating a canvas 
- inserting ```buttons()``` , ```labels()``` ,```grid()``` and ```.img()``` inside the canvas
- creating the ```windows.Mainloop()```
- importing ```item.config()``` and ```windows.after()```
- creating necessary functions for the construction and scheduling of the timer
- setting the layout configuration and making some global variables inside the function 
- setting the timer function 

# some code snippets 

```def start_timer():
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
        tick_label.grid(column=1, row=3)```
        
        
        
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


          start_button=Button(width=5,text="start",fg=RED,command=start_timer)
          start_button.grid(columns=1,row=3)

          tick_label=Label(text="✓",bg=YELLOW,fg=GREEN,font=(FONT_NAME,25,"bold"))
          tick_label.grid(column=1,row=3)

          reset_button=Button(width=10,text="reset",fg=RED,command=reset_the_timer)
          reset_button.grid(column=3,row=3)
          
    


        
        

        

    
  
