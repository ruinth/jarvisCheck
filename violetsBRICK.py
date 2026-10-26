from tkinter import *

window = Tk()
window.attributes('-fullscreen', True,)
width = window.winfo_screenwidth()
width2 = width/2
height = window.winfo_screenheight()
height2= height/2
asked_questions = 0
chores_list = ["dishes","wash laundry", "put away laundry", "litter box", "partition","trash taken out", "living room", "bedroom"]

def do_exit():
    global pressed_f4
    if pressed_f4:  # Deny if Alt-F4 is pressed
        pressed_f4 = False  # Reset variable
def alt_f4(event):  # Alt-F4 is pressed
    global pressed_f4
    pressed_f4 = True
window.bind('<Alt-F4>', alt_f4)
window.protocol("WM_DELETE_WINDOW",do_exit)

def close_window():
    window.quit()

def start_check():
    greeting_label.pack_forget()
    this_tool_label.pack_forget()
    access_will_label.place_forget()
    start_checklist_button.place_forget()
    work_today_label.place(x=width2,y=height2-100, anchor="center")
    yes_work_box.place(x=width2-40,y=height2,anchor="center")
    no_work_box.place(x=width2+40,y=height2,anchor="center")
    next_question_button.place(x=width2, y=height2+50)

def next_question():
    global asked_questions, chores_list
    asked_questions+=1
    if asked_questions == 1:
        work_today_label.place_forget()
        yes_work_box.place_forget()
        no_work_box.place_forget()
        work_or_fun_label.place(x=width2,y=height2-100, anchor="center")
        for_work_box.place(x=width2-40,y=height2,anchor="center")
        for_fun_box.place(x=width2+40,y=height2,anchor="center")
    if asked_questions == 2:
        work_or_fun_label.place_forget()
        for_work_box.place_forget()
        for_fun_box.place_forget()
        chores_header_label.place(x=600,y=200)
        done_chore_label.place(x=width2+200, y=205,)
        not_done_chore_label.place(x=width2+240, y=205)

        for index in range(len(chores_list)):
            chore_label = Label(window,
            text=chores_list[index],
            font=("Helvetica", 20))
            chore_label.place(x=600,y=260+(60*index))
        for index in range(len(chores_list)):
            yes_check = IntVar()
            yes_button = Checkbutton(window,
            variable=yes_check)
            yes_button.place(x=width2+200, y=260+(60*index))
        for index in range(len(chores_list)):
                    no_check = IntVar()
                    no_button = Checkbutton(window,
                    variable=no_check)
                    no_button.place(x=width2+240, y=260+(60*index))

        next_question_button.place_forget()
        thats_not_me_button.config(text="exit checklist")

greeting_label = Label(window, text=(f"Hello violet <3"),
                   font = ("Helvetica", 50))

this_tool_label= Label(window, text=("this is a tool that you designed,\n"
                                    "it will help hold yourself accountable"),
                   font = ("Helvetica", 10))

access_will_label = Label(window, text=("access to the computer is not\n"
                                        "dependant on your answers"),
                   font = ("Helvetica", 15))

work_today_label = Label(window, text="do you work today?",
                         font = ("Helvetica", 30))

work_or_fun_label = Label(window, text="is this for work, or fun",
                         font = ("Helvetica", 30))

start_checklist_button = Button(window, text="let's start", 
                            font = ("Helvetica", 30),
                            command=start_check)      
     
thats_not_me_button = Button(window, text="i'm not\nviolet", 
                            font = ("Helvetica", 40),
                            command=close_window,
                            bg="#FF1100")  

next_question_button = Button(window, text="next",
                              font=("Helvetica",20),
                              command = next_question)

yes_checked = IntVar()
no_checked = IntVar()
yes_work_box = Checkbutton(window, text="yes", variable=yes_checked,
                  font = ("Helvetica", 15))
no_work_box = Checkbutton(window, text = "no", variable= no_checked,
                 font = ("Helvetica", 15))
ffun_box = IntVar()
fwork_box = IntVar()
for_work_box = Checkbutton(window, text="work", variable=fwork_box,
                  font = ("Helvetica", 15))
for_fun_box = Checkbutton(window, text = "fun", variable= ffun_box,
                 font = ("Helvetica", 15))

chores_header_label = Label(window, text= "Chores",
                            font= ("Helvetica", 30))
done_chore_label = Label(window, text="done",
                         font=("Helvetica", 10))
not_done_chore_label = Label(window, text="not done",
                         font=("Helvetica", 10))

greeting_label.pack(pady=30)
this_tool_label.pack()
access_will_label.place(x=width2,y=450, anchor=CENTER)
start_checklist_button.place(x=width2, y=height2, anchor= CENTER)
thats_not_me_button.place(x=width2, y=750, anchor=CENTER)

window.mainloop()