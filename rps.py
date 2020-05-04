import random
import tkinter as tk
from tkinter import ttk
from tkinter import *
from subprocess import call

window = tk.Tk()
window.geometry('400x550')
window.title('Rock Paper Scissor')
USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ''
COMP_CHOICE = ''

def choice_to_number(choice):
    rps = {'rock':0,'paper':1,'scissor':2}
    return rps[choice]
def number_to_choice(number):
    rps = {0:'rock',1:'paper',2:'scissor'}
    return rps[number]

def random_computer_choice():
    return random.choice(['rock','paper','scissor'])

def result(human_choice,comp_choice):
    global USER_SCORE
    global COMP_SCORE
    user = choice_to_number(human_choice)
    comp = choice_to_number(comp_choice)
    if (user==comp):
        print('Tie')
    elif ((user-comp)%3==1):
        print('You Won')
        USER_SCORE+=1
    else:
        print('Computer won')
        COMP_SCORE+=1
    text_area = tk.Text(master=window,height=8,width=30,bg='#FFFF99')
    text_area.grid(column=0,row=4)
    answer = "your Choice: {uc} \nComputer Choice: {cc}\nYour Score: {us}\nComputer Score: {cs}".format(uc=USER_CHOICE,cc=COMP_CHOICE,us=USER_SCORE,cs=COMP_SCORE)
    text_area.insert(tk.END,answer)

def rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'rock'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)
def paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'paper'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)

def scissor():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'scissor'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)

def feedback():
    call(['python','feedback.py'])
    
image=PhotoImage(file = 'rps.gif')

label_image=tk.Label(image=image)
label_image.grid(column=0,row=0)

button1 = tk.Button(text="       Rock     ",bg="#fab1a0",command=rock)
button1.grid(column=0,row=1)

button2 = tk.Button(text="       paper     ",bg="skyblue",command=paper)
button2.grid(column=0,row=2)

button3 = tk.Button(text="       Scissor    ",bg="lightgreen",command=scissor)
button3.grid(column=0,row=3)
window.mainloop()
    
